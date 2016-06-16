
--Drops usados para teste
drop table comite cascade;
drop table orgao_imprensa cascade;
drop table tipo_credencial cascade;
drop table credencial cascade;
drop table profissional_imprensa cascade;
drop table limites_comite cascade;
drop table limites_oi cascade;
drop function verifica_limites_comite(integer, character varying, integer) CASCADE;
drop function verifica_limites_oi(integer, character varying) CASCADE;



--Criação dos procedures usados nos CHECKs da tabela credencial e limites_oi


-- Ao ser alocada certa quantidade de credenciais de certo tipo para certo órgão de imprensa via tabela limites_oi,
-- é preciso verificar se o total de alocações de credenciais daquele tipo não excede o total disponível para o comitê
-- (determinado na tabela limites_comite).
CREATE OR REPLACE FUNCTION verifica_limites_comite (orgao_id integer, tipo_cred varchar(4), qtd integer) RETURNS boolean AS $$
DECLARE
	alocado integer;
	limite integer;
	com varchar(50);
BEGIN

	-- Obtendo o comitê do órgão de imprensa em questão.
	select comite
	into com
	from orgao_imprensa oi
	where oi.id = orgao_id;

	-- Contando a quantidade de credenciais do tipo em questão já alocadas pelo comitê.
	select sum(lim.quantidade)
	into alocado
	from limites_oi lim join orgao_imprensa oi on lim.orgao_imprensa = oi.id
	where oi.comite = com and lim.tipo_credencial = tipo_cred;

	IF (alocado IS NULL) THEN
		alocado = 0;
	END IF;

	-- Obtendo o limite do comitê para o tipo de credencial em questão.
	select lim.quantidade
	into limite
	from limites_comite lim
	where tipo_cred = lim.tipo_credencial and lim.comite = com;

	IF (limite IS NULL) THEN	-- Nunca deve ocorrer, pois a inserção na tabela limites_comite é automática via trigger.
		limite = 0;
	END IF;
	
	IF (alocado+qtd <= limite) THEN
		RETURN TRUE;
	END IF;

	RETURN FALSE;
END;
$$ LANGUAGE plpgsql;

-- Para uma nova credencial de certo tipo ser criada e associada a certo órgão de imprensa, é preciso verificar se 
-- o comitê ao qual o OI está associado ainda tem credenciais disponíveis que sejam daquele tipo e estejam alocadas ao OI em questão.
-- Em outras palavras, é preciso verificar se o OI já não atingiu o limite de credenciais do tipo em questão que está especificado
-- em limites_oi.
CREATE OR REPLACE FUNCTION verifica_limites_oi (orgao_id integer, tipo_cred varchar(4)) RETURNS boolean AS $$
DECLARE
	limite integer;
	usado integer;
BEGIN
	
	-- Contando a quantidade de credenciais desse tipo ja alocadas pelo comitê ao órgão de imprensa em questão.
	select count(*)
	into usado
	from credencial cred
	where cred.orgao_imprensa = orgao_id and cred.tipo = tipo_cred;

	-- Obtendo o limite que o comitê estabeleceu para o tipo de credencial e órgão de imprensa envolvidos.
	select lim.quantidade
	into limite
	from limites_oi lim
	where lim.tipo_credencial = tipo_cred and lim.orgao_imprensa = orgao_id;

	IF (usado < limite) THEN
		RETURN TRUE;
	END IF;

	RETURN FALSE;
END;
$$ LANGUAGE plpgsql;



--Criação das tabelas do schema

CREATE TABLE comite
(
	pais varchar(30) DEFAULT '-' NOT NULL,	-- O traço (-) representa o Comitê Paralímpico Internacional (IPC), o qual não tem país.
	nome varchar(50),
	presidente varchar(70),
	email_contato varchar(80),
	endereco varchar(80),
	PRIMARY KEY(nome),
	UNIQUE(pais)
);

CREATE TABLE orgao_imprensa
(
	nome varchar(50) NOT NULL,
	comite varchar(50) NOT NULL, 
	endereco varchar(100),
	nome_representante varchar(70),
	email_representante varchar(80),
	id serial,
	PRIMARY KEY(id),
	FOREIGN KEY(comite) REFERENCES comite(nome) ON DELETE CASCADE,
	UNIQUE(nome, comite)
);

CREATE TABLE tipo_credencial
(
	sigla varchar(4),
	funcao varchar(30) NOT NULL,
	direito_transmissao char(1) NOT NULL,
	PRIMARY KEY (sigla),
	CHECK(upper(direito_transmissao) = 'S' or upper(direito_transmissao) = 'N')
);

CREATE TABLE credencial
(
	codigo serial,
	tipo varchar(4) NOT NULL,
	orgao_imprensa integer NOT NULL,
	PRIMARY KEY(codigo),
	FOREIGN KEY(orgao_imprensa) REFERENCES orgao_imprensa(id) ON DELETE CASCADE,
	FOREIGN KEY (tipo) REFERENCES tipo_credencial(sigla) ON DELETE CASCADE--,
	--CHECK(verifica_limites_oi(orgao_imprensa, tipo))
	--O CHECK garante que não será possível vincular mais credenciais de certo tipo a um OI do que é especificado na tabela limites_oi
);

CREATE TABLE profissional_imprensa
(
	passaporte char(8),
	email varchar(80),
	cpf char(11),
	data_nascimento date,
	nacionalidade varchar(20),
	funcao varchar(30) NOT NULL,
	nome varchar(70),
	credencial integer,
	orgao_imprensa integer NOT NULL,
	PRIMARY KEY(credencial),
	UNIQUE(cpf),
	FOREIGN KEY(credencial) REFERENCES credencial(codigo) ON DELETE CASCADE,
	FOREIGN KEY (orgao_imprensa) REFERENCES orgao_imprensa(id) ON DELETE CASCADE
);

CREATE TABLE limites_comite
(
	comite varchar(50),
	tipo_credencial varchar(4),
	quantidade integer NOT NULL DEFAULT 0,
	PRIMARY KEY(comite, tipo_credencial),
	FOREIGN KEY(tipo_credencial) REFERENCES tipo_credencial(sigla) ON DELETE CASCADE,
	FOREIGN KEY(comite) REFERENCES comite(nome) ON DELETE CASCADE
);

CREATE TABLE limites_oi
(
	tipo_credencial varchar(4),
	orgao_imprensa integer,
	quantidade integer NOT NULL DEFAULT 0,
	PRIMARY KEY (tipo_credencial, orgao_imprensa),
	FOREIGN KEY (tipo_credencial) REFERENCES tipo_credencial(sigla) ON DELETE CASCADE,
	FOREIGN KEY (orgao_imprensa) REFERENCES orgao_imprensa(id) ON DELETE CASCADE,
	CHECK(verifica_limites_comite(orgao_imprensa, tipo_credencial, quantidade))
	--O CHECK garante que não será possível que um comitê aloque a seus OIs mais credenciais de certo tipo do que possui disponível (especificado na tabela limites_comite)
);



--Criação dos triggers responsáveis pela realização das devidas inserções nas tabelas limites_comite e limites_oi na criação de um novo comitê, OI, ou tipo de credencial


-- Quando um comitê é inserido, a tabela limites_comite (que para cada par comite, tipo_de_credencial associa
-- o número de credenciais daquele tipo disponíveis para o comitê) precisa ser atualizada para guardar os limites do novo comitê.
-- Para cada tipo de credencial existente, é adicionada uma nova entrada em limites_comite para o comitê recém adicionado.
-- Note que o valor default para o limite é zero.
CREATE OR REPLACE FUNCTION inserir_limites_comite() RETURNS TRIGGER AS $$
DECLARE
	tipo varchar(4);
BEGIN
	for tipo in select sigla from tipo_credencial loop
		insert into limites_comite(comite, tipo_credencial, quantidade) values (new.nome, tipo, default);
	end loop;
	RETURN new;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER comite_trigger AFTER INSERT ON comite
FOR EACH ROW EXECUTE PROCEDURE inserir_limites_comite();


-- Análogo acima vale quando um novo orgão de imprensa é adicionado: quando um novo OI é criado, para cada tipo de credencial existente, um novo registro
-- em limites_oi precisa ser criado.
CREATE OR REPLACE FUNCTION inserir_limites_oi() RETURNS TRIGGER AS $$
DECLARE
	tipo varchar(4);
BEGIN
	for tipo in select sigla from tipo_credencial loop
		insert into limites_oi(tipo_credencial, orgao_imprensa, quanitdade) values (tipo, new.id, default);
	end loop;
	RETURN new;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER oi_trigger AFTER INSERT ON orgao_imprensa
FOR EACH ROW EXECUTE PROCEDURE inserir_limites_oi();


-- Quando um novo tipo de credencial é adicionado, ambas as tabelas limites_comite
-- e limites_oi devem ser atualizadas. A primeira com uma nova tupla para cada comitê, e a
-- segunda com uma nova tupla para cada órgão de imprensa.
CREATE OR REPLACE FUNCTION inserir_limites_tipo() RETURNS TRIGGER AS $$
DECLARE
c varchar(50);
oi integer;
BEGIN
	for c in select nome from comite loop
		insert into limites_comite(comite, tipo_credencial) values (c, new.sigla);
	end loop;
	for oi in select id from orgao_imprensa loop
		insert into limites_oi(tipo_credencial, orgao_imprensa) values (new.sigla, oi);
	end loop;
	RETURN new;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tipo_trigger AFTER INSERT ON tipo_credencial
FOR EACH ROW EXECUTE PROCEDURE inserir_limites_tipo();

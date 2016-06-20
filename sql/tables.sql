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
	UNIQUE(nome)
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
	FOREIGN KEY (tipo) REFERENCES tipo_credencial(sigla) ON DELETE CASCADE,
	CHECK(verifica_limites_oi(orgao_imprensa, tipo))
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

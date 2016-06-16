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
		insert into limites_oi(tipo_credencial, orgao_imprensa, quantidade) values (tipo, new.id, default);
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

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

	-- Contando a quantidade de credenciais do tipo em questão já alocadas pelo comitê (não conta as para o orgão orgao_id pois este será atualizado)
	select sum(lim.quantidade)
	into alocado
	from limites_oi lim join orgao_imprensa oi on lim.orgao_imprensa = oi.id
	where oi.comite = com and lim.tipo_credencial = tipo_cred and oi.id <> orgao_id;

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

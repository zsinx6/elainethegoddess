-- Alguns testes do banco de dados. De preferência rodar com o banco de dados vazio.
-- Note que algumas inserções falham de propósito - são testes de CHECKs de tabelas

insert into tipo_credencial(sigla, funcao, direito_transmissao) values ('ET', 'Técnico', 'N');
insert into tipo_credencial(sigla, funcao, direito_transmissao) values ('EC', 'Cameraman', 'S');

insert into comite(pais, nome, presidente) values ('Rússia', 'Paralympic Committee of Russia', 'Mr. Vladimir Putin');	-- Trigger causa a criação de 2 tuplas em limites_comite
insert into comite(pais, nome, presidente) values ('Estados Unidos', 'US Paralympics', 'Lawrence F. Probst III');		-- Idem acima
insert into comite(pais, nome, presidente) values ('Grã-Bretanha', 'British Paralympic Association', 'Tim Reddish'); 	-- Idem acima

insert into tipo_credencial(sigla, funcao, direito_transmissao) values ('ER', 'Radialista', 'N'); 	--Trigger causa a criação de 3 tuplas em limites_comite 

insert into orgao_imprensa(nome, comite, id) values ('Washington Post', 'US Paralympics', 50001);				--Trigger causa a criação de 3 tuplas em limites_oi
insert into orgao_imprensa(nome, comite, id) values ('ITAR-TASS', 'Paralympic Committee of Russia', 50002);	--Idem acima
insert into orgao_imprensa(nome, comite, id) values ('The Guardian', 'British Paralympic Association', 50003);	--Idem acima
insert into orgao_imprensa(nome, comite, id) values ('Reuters', 'International Paralympic Comittee', 50004); 	--Idem acima (note que o IPC é inserido de antemão, no triggers.sql)
insert into orgao_imprensa(nome, comite, id) values ('EFE', 'International Paralympic Comittee', 50005); 		--Idem acima 

--Fazendo o comitê internacional ter 100 credenciais disponíveis para cada um dos três tipos de credenciais definidos
update limites_comite set
quantidade = 100
where comite = 'International Paralympic Comittee';

--Comitê internacional fornecendo 70 credenciais do tipo 'E' à Reuters
update limites_oi set
quantidade = 70
where orgao_imprensa = 50004 and tipo_credencial = 'ER';

--Comitê internacional tenta fornecer 50 credenciais do tipo 'E' à EFE: erro, pois ele só possui 30 credenciais disponíveis desse tipo
update limites_oi set
quantidade = 50
where orgao_imprensa = 50005 and tipo_credencial = 'ER';

-- US Paralympics ganha 10 credenciais do tipo Ec
update limites_comite set
quantidade = 10
where comite = 'US Paralympics' and tipo_credencial = 'EC';

--US Paralympics aloca 1 credencial do tipo EC a Washington Post (id 1)
update limites_oi set
quantidade = 1
where orgao_imprensa = 50001 and tipo_credencial = 'EC';

--US Paralympics fornece sua credencial a Washington Post
insert into credencial(codigo, tipo, orgao_imprensa) values (10300, 'EC', 50001); 

--US Paralympics tenta fornecer outra credencial a Washington Post isso
-- não é possível pois já excedeu o limite de credenciais Ec alocadas para tal órgão 
insert into credencial(codigo, tipo, orgao_imprensa) values (10301, 'EC', 50001);

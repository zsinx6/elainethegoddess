insert into tipo_credencial(sigla, funcao, direito_transmissao) values ('Ep', 'Fotógrafo jornalístico', 'N');
insert into tipo_credencial(sigla, funcao, direito_transmissao) values ('Ec', 'Cameraman', 'S');

insert into comite(pais, nome) values ('Brasil', 'Comitê Paralímpico Brasileiro');			-- Trigger causa a criação de 2 tuplas em limites_comite
insert into comite(pais, nome) values ('Estados Unidos', 'US Paralympics');					-- Idem acima
insert into comite(pais, nome) values ('Grã-Bretanha', 'British Paralympic Association'); 	-- Idem acima
insert into comite(nome) values ('International Paralympic Comitee');						-- Idem acima, pais setado para o default ("-").

insert into tipo_credencial(sigla, funcao, direito_transmissao) values ('E', 'Repórter esportivo', 'N'); --Trigger causa a criação de 3 tuplas em limites_comite 

insert into orgao_imprensa(nome, comite, id) values ('Washington Post', 'US Paralympics', 1);	--Trigger causa a criação de 3 tuplas em limites_oi
insert into orgao_imprensa(nome, comite, id) values ('Agência Brasil', 'Comitê Paralímpico Brasileiro', 2);	--Idem acima
insert into orgao_imprensa(nome, comite, id) values ('The Guardian', 'British Paralympic Association', 3);	--Idem acima
insert into orgao_imprensa(nome, comite, id) values ('Reuters', 'International Paralympic Comitee', 4); --Idem acima
insert into orgao_imprensa(nome, comite, id) values ('EFE', 'International Paralympic Comitee', 5); --Idem acima

--Fazendo o comitê internacional ter 100 credenciais disponíveis para cada um dos três tipos de credenciais definidos
update limites_comite set
quantidade = 100
where comite = 'International Paralympic Comitee';

--Comitê internacional fornecendo 70 credenciais do tipo 'E' à Reuters
update limites_oi set
quantidade = 70
where orgao_imprensa = 4 and tipo_credencial = 'E';

--Comitê internacional tenta fornecer 50 credenciais do tipo 'E' à EFE: erro, pois ele só possui 30 credenciais disponíveis desse tipo
update limites_oi set
quantidade = 50
where orgao_imprensa = 5 and tipo_credencial = 'E';

-- US Paralympics ganha 10 credenciais do tipo Ec
update limites_comite set
quantidade = 10
where comite = 'US Paralympics' and tipo_credencial = 'Ec';

--US Paralympics aloca 1 credencial do tipo EC a Washington Post (id 1)
update limites_oi set
quantidade = 1
where orgao_imprensa = 1 and tipo_credencial = 'Ec';

--US Paralympics fornece sua credencial a Washington Post
insert into credencial(codigo, tipo, orgao_imprensa) values (10300, 'Ec', 1); 

--US Paralympics tenta fornecer outra credencial a Washington Post isso
-- não é possível pois já execdeu o limite de credenciais Ec alocadas para tal órgão 
insert into credencial(codigo, tipo, orgao_imprensa) values (10301, 'Ec', 1);

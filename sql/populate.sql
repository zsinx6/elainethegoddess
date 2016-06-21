-- Popula o banco de dados. De preferência rodar com o banco de dados vazio.

INSERT INTO comite(pais, nome, presidente, email_contato, endereco) values ('Brazil', 'Comite Paraolimpico Brasileiro', 'Rodrigo Weigert', 'brazil@brazil.com', 'Rua do comite, 222, Rio de Janeiro/RJ');

INSERT INTO comite(pais, nome, presidente, email_contato, endereco) values ('Portugal', 'Comite Paraolimpico de Portugal', 'Joaquim Queiroz', 'correio@comiteolimpicoportugal.pt', 'Travessa da Memoria, 36 - 1300-403, Lisboa') ;


INSERT INTO orgao_imprensa(nome, comite, endereco, nome_representante, email_representante, id) VALUES ('Rede Globo', 'Comite Paraolimpico Brasileiro', 'R. Von Martius, 22 - Rio de Janeiro/RJ', 'Joao da Silva', 'joao@globo.com', 10001);
INSERT INTO orgao_imprensa(nome, comite, endereco, nome_representante, email_representante, id) VALUES ('SIC', 'Comite Paraolimpico de Portugal', 'R. la em portugal, 7 - Lisboa', 'Joaquim Manoel', 'joaquim@sic.pt', 10002);

INSERT INTO tipo_credencial(sigla, funcao, direito_transmissao) VALUES ('E', 'Jornalista', 'S');

INSERT INTO tipo_credencial(sigla, funcao, direito_transmissao) VALUES ('EP', 'Fotografo', 'S');

UPDATE limites_comite SET quantidade = 10 WHERE comite = 'Comite Paraolimpico Brasileiro' AND tipo_credencial='E';
UPDATE limites_comite SET quantidade = 10 WHERE comite = 'Comite Paraolimpico Brasileiro' AND tipo_credencial='EP';
UPDATE limites_comite SET quantidade = 10 WHERE comite = 'Comite Paraolimpico de Portugal' AND tipo_credencial='EP';
UPDATE limites_comite SET quantidade = 10 WHERE comite = 'Comite Paraolimpico de Portugal' AND tipo_credencial='E';

UPDATE limites_oi SET quantidade=5 WHERE tipo_credencial='E' AND orgao_imprensa=10001;
UPDATE limites_oi SET quantidade=5 WHERE tipo_credencial='E' AND orgao_imprensa=10002;
UPDATE limites_oi SET quantidade=5 WHERE tipo_credencial='EP' AND orgao_imprensa=10001;
UPDATE limites_oi SET quantidade=5 WHERE tipo_credencial='EP' AND orgao_imprensa=10002;

INSERT INTO credencial(codigo, tipo, orgao_imprensa) VALUES (20001, 'E', 10001);

INSERT INTO credencial(codigo, tipo, orgao_imprensa) VALUES (20002, 'EP', 10001);

INSERT INTO credencial(codigo, tipo, orgao_imprensa) VALUES (20003, 'E', 10002);

INSERT INTO credencial(codigo, tipo, orgao_imprensa) VALUES (20004, 'EP', 10002);

INSERT INTO profissional_imprensa(passaporte, email, cpf, data_nascimento, nacionalidade, funcao, nome, credencial, orgao_imprensa) VALUES ('123', 'danilo@globo.com', '35061924889', '10/09/1992', 'brazilian', 'Jornalista', 'Danilo Tedeschi', 20001, 10001); 
INSERT INTO profissional_imprensa(passaporte, email, cpf, data_nascimento, nacionalidade, funcao, nome, credencial, orgao_imprensa) VALUES ('321', 'lucas@sic.pt', '', '10/07/1994', 'portuguese', 'Fotografo', 'Lucas Carvalho', 20004, 10002);

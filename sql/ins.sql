--popula o banco de dados

INSERT INTO comite values ('Brazil', 'Comite Paraolimpico brasileiro', 'Rodrigo Weigert', 'brazil@brazil.com', 'rua do comite, 222, Rio de Janeiro/RJ');

INSERT INTO comite values ('Portugal', 'Comite Paraolimpico de Portual', 'Joaquim Queiroz', 'correio@comiteolimpicoportugal.pt', 'Travessa da Memoria, 36 - 1300-403, Lisboa') ;


INSERT INTO orgao_imprensa VALUES ('Rede Globo', 'Comite Paraolimpico brasileiro', 'R. Von Martius, 22 - Rio de Janeiro/RJ', 'Joao da Silva', 'joao@globo.com', 1);
INSERT INTO orgao_imprensa VALUES ('SIC', 'Comite Paraolimpico de Portual', 'R. la em portugal, 7 - Lisboa', 'Joaquim Manoel', 'joaquim@sic.pt', 2);

INSERT INTO tipo_credencial VALUES ('E', 'Jornalista', 'S');

INSERT INTO tipo_credencial VALUES ('EP', 'Fotografo', 'S');


INSERT INTO credencial VALUES (1, 'E', 1);

INSERT INTO credencial VALUES (2, 'EP', 1);

INSERT INTO credencial VALUES (3, 'E', 2);

INSERT INTO credencial VALUES (4, 'EP', 2);

INSERT INTO profissional_imprensa VALUES ('123', 'danilo@globo.com', '35061924889', '10/09/1992', 'brazilian', 'Jornalista', 'Danilo Tedeschi', 1, 1); 
INSERT INTO profissional_imprensa VALUES ('321', 'lucas@sic.pt', '', '10/07/1994', 'portuguese', 'Fotografo', 'Lucas Carvalho', 4, 2);


UPDATE limites_comite SET quantidade = 10 WHERE comite = 'Comite Paraolimpico brasileiro' AND tipo_credencial='E';
UPDATE limites_comite SET quantidade = 10 WHERE comite = 'Comite Paraolimpico de Portugal' AND tipo_credencial='EP';
UPDATE limites_comite SET quantidade = 10 WHERE comite = 'Comite Paraolimpico de Portual' AND tipo_credencial='EP';
UPDATE limites_comite SET quantidade = 10 WHERE comite = 'Comite Paraolimpico de Portual' AND tipo_credencial='E';

UPDATE limites_oi SET quantidade=5 WHERE tipo_credencial='E' AND orgao_imprensa=1;
UPDATE limites_oi SET quantidade=5 WHERE tipo_credencial='E' AND orgao_imprensa=2;
UPDATE limites_oi SET quantidade=5 WHERE tipo_credencial='EP' AND orgao_imprensa=1;
UPDATE limites_oi SET quantidade=5 WHERE tipo_credencial='EP' AND orgao_imprensa=2;

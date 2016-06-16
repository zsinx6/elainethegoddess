Para montar a base de dados, execute os scripts nessa ordem (no terminal do postgres o comando é \i):
	procedures.sql tables.sql triggers.sql

Depois disso pode se quiser rodar o teste que eu montei, insert.sql. Note que tem alguns comandos que é para falhar de propósito.

Por enquanto, alterações nas tabelas de limites podem ser feitas livremente. Se um OI tem 50 credenciais do tipo X, todas já alocadas (isso é, já existem 50 tuplas na tabela credencial) e a tabela limites_oi é alterada para 25 credenciais, a alteração é feita. Mas nenhuma nova credencial poderá ser adicionada enquanto menos de 26 não forem deletadas da tabela credencial, pois o check sempre vai falhar.

create database if not exists fatec;

use fatec;

create table contatos(
email varchar(60),
assunto varchar(60),
descricao varchar(500)
);

select * from contatos;
describe contatos;
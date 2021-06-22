drop database if exists covid_dataset;
create database covid_dataset;

use covid_dataset;

drop table if exists record;
create table record (
    id int primary key not null auto_increment,
    pruid varchar(10),
    prname varchar(25),
    prnameFR varchar(25),
    date varchar(10),
    numconf varchar(10),
    numprob varchar(10),
    numdeaths varchar(10),
    numtotal varchar(10),
    numtoday varchar(10),
    ratetotal varchar(10)
);
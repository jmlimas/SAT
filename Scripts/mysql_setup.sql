-- Create Database.
create database satdb;

-- Create a new user to protect the Database Server and to be used only with
-- the SAT system.

USE satdb;

grant usage on *.* to satuser@localhost identified by 'satpassword';
grant all privileges on satdb.* to satuser@localhost;
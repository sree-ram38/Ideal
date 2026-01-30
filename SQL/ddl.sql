

create table student (
name varchar(50),
department varchar(100),
marks_scored int
)

insert into student value("sree","computer science",499)
--to add a column 
alter table student add column city varchar(100)
--to change the column name 
alter table student change marks_scored marks int 
--to change the datatype of the specific column
alter table student change marks marks varchar(10) 
--drop will delete the specific column or table
drop table student
--truncate is used to delete all the data inside the table that means all the data inside the column will be deleted
truncate table student 
--this is used to view the table
select * from student 
-- this is DDL(Data Definition Language)command(create, alter, drop, truncate)These are the ddl commands
--DDL commands - create, alter, drop, truncate  
  
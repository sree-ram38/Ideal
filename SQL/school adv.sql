create database school;
create table marks (
Roll_No int,
Name varchar(15),
Tamil int,
English int,
Maths int,
Science int,
Social_Science int,
primary key (roll_no)
)
insert into marks value(1,"sree",85,78,68,77,89)
insert into marks value(2,"Ram",58,86,87,76,88)
insert into marks value(3,"Aswin",99,81,66,51,90)
insert into marks value(4,"Hari",92,71,75,58,64)
insert into marks value(5,"Siva",79,83,73,88,56)
insert into marks value(6,"Abishek",65,78,68,77,89)
insert into marks value(7,"Vinu",80,68,78,47,59)
insert into marks value(8,"Gokul",75,82,88,87,99)
insert into marks value(9,"Thalaiva",65,58,88,67,79)
insert into marks value(10,"krishna",45,58,25,67,68

alter table marks drop primary key;
alter table marks add primary key(Roll_No);

select * from marks where Roll_No=4

select Name from marks;

alter table marks add Total int;

update marks set Total = Tamil + English + Maths + Science + Social_Science;

select Roll_No,
Tamil,
English,
Maths,
Science,
Social_Science,(Tamil + English + Maths + Science + Social_Science ) as Total from marks;


use school;
select * from marks;
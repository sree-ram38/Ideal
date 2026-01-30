show databases;
use school;
CREATE TABLE mark(
id int,
name varchar(30),
price int(4),
primary key(id)
)
show tables;
desc mark;





















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
);
insert into marks value(1,"sree",85,78,68,77,89);
insert into marks value(2,"Ram",58,86,87,76,88);
insert into marks value(3,"Aswin",99,81,66,51,90);
insert into marks value(4,"Hari",92,71,75,58,64);
insert into marks value(5,"Siva",79,83,73,88,56);
insert into marks value(6,"Abishek",65,78,68,77,89);
insert into marks value(7,"Vinu",80,68,78,47,59);
insert into marks value(8,"Gokul",75,82,88,87,99);
insert into marks value(9,"Thalaiva",65,58,88,67,79);
insert into marks value(10,"krishna",45,58,25,67,68);

alter table marks change Name Name_of_the_student varchar(100);

update marks set Name_of_the_student="Akash" where Name_of_the_student="Ram";

alter table marks drop primary key;
alter table marks add primary key(Roll_No);

select * from marks where Roll_No=4;

select Name from marks;

alter table marks add Total int;

update marks set Total = Tamil + English + Maths + Science + Social_Science;

select Roll_No,
Name,
Tamil,
English,
Maths,
Science,
Social_Science,(Tamil + English + Maths + Science + Social_Science ) as Total from marks;

alter table marks add column Average int;

update marks set Average = (Tamil + English + Maths + Science + Social_Science)/5;

alter table marks add column class varchar(10);

alter table marks add column result varchar(10);

update marks set class=case when Average > 35 and Average <60 then 'Third' 
when Average > 60 and Average <80 then 'Second' 
when Average > 80  then 'First' end;

update marks set result=case when (Tamil < 35 or English < 35 or Maths < 35 or Science < 35 or Social_Science < 35) then 'Fail' 
else 'pass' end;

use school;
select * from marks;




create table studentInformation(
Roll_No int,
Name_of_the_student varchar(15),
Standard varchar(20),
Division varchar(20),
Parent_Name varchar(50),
Address varchar(100),
Contact varchar(50)
);

insert into studentInformation value
(1,"sree","XI","A","Iyyappan","29 pillaiyar kovil","1236547894"),
(2,"Akash","XI","B","Ramachandran","32 east avenue","4567891236"),
(3,"Aswin","XI","A","Thanu","14 cross street","9756321456"),
(4,"Hari","XI","C","Mani","church street pallivilai","4567898527"),
(5,"Siva","XI","B","Thanumalaiyan","32 near palayaru mylaudy","7539512586"),
(6,"Abishek","XI","A","Murugesan","12 arasu tree parvathipuram","8529637419"),
(7,"Vinu","XI","C","Gopal","56 avenue porur","9517417891"),
(8,"Gokul","XI","A","Chidambaram","12/6 keelatheru","8524561597"),
(9,"Thalaiva","XI","B","Krishnan","28 krishnan kovil street","3693217895"),
(10,"Krishna","XI","C","Rajan","23 near tank road mylady","5896245789");

select * from studentInformation;

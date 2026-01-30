create database school;


create table studentInformation(
student_id varchar(10),
Name_of_the_student varchar(15),
Standard varchar(20),
Division varchar(20),
Parent_Name varchar(50),
Address varchar(100),
Contact varchar(50),
primary key(student_id)
);

insert into studentInformation value
(41,"sree","XI","A","Iyyappan","29 pillaiyar kovil","1236547894"),
(42,"Akash","XI","B","Ramachandran","32 east avenue","4567891236"),
(43,"Aswin","XI","A","Thanu","14 cross street","9756321456"),
(44,"Hari","XI","C","Mani","church street pallivilai","4567898527"),
(45,"Siva","XI","B","Thanumalaiyan","32 near palayaru mylaudy","7539512586"),
(46,"Abishek","XI","A","Murugesan","12 arasu tree parvathipuram","8529637419"),
(47,"Vinu","XI","C","Gopal","56 avenue porur","9517417891"),
(48,"Gokul","XI","A","Chidambaram","12/6 keelatheru","8524561597"),
(49,"Thalaiva","XI","B","Krishnan","28 krishnan kovil street","3693217895"),
(50,"Krishna","XI","C","Rajan","23 near tank road mylady","5896245789");



create table marks (
student_id varchar(10),
Name varchar(15),
Tamil int,
English int,
Maths int,
Science int,
Social_Science int,
foreign key(student_id) references studentInformation(student_id)
);
insert into marks value(41,"sree",85,78,68,77,89);
insert into marks value(42,"Akash",58,86,87,76,88);
insert into marks value(43,"Aswin",99,81,66,51,90);
insert into marks value(44,"Hari",92,71,75,58,64);
insert into marks value(45,"Siva",79,83,73,88,56);
insert into marks value(46,"Abishek",65,78,68,77,89);
insert into marks value(47,"Vinu",80,68,78,47,59);
insert into marks value(48,"Gokul",75,82,88,87,99);
insert into marks value(49,"Thalaiva",65,58,88,67,79);
insert into marks value(50,"krishna",45,58,25,67,68);

-- alter table marks change Name Name_of_the_student varchar(100);
-- update marks set Name_of_the_student="Akash" where Name_of_the_student="Ram";

-- alter table marks drop primary key;
-- alter table marks add primary key(Roll_No);

-- select * from marks where Roll_No=4
-- select Name from marks;

alter table marks add Total int;
update marks set Total = Tamil + English + Maths + Science + Social_Science;

-- select Roll_No,
-- Name,
-- Tamil,
-- English,
-- Maths,
-- Science,
-- Social_Science,(Tamil + English + Maths + Science + Social_Science ) as Total from marks;

alter table marks add column Average int;

update marks set Average = (Tamil + English + Maths + Science + Social_Science)/5;

alter table marks add column class varchar(10);

alter table marks add column result varchar(10);

update marks set class=case when Average > 35 and Average <60 then 'Third' 
when Average > 60 and Average <80 then 'Second' 
when Average > 80  then 'First' end;

update marks set result=case when (Tamil < 35 or English < 35 or Maths < 35 or Science < 35 or Social_Science < 35) then 'Fail' 
else 'pass' end;







select Name_of_the_student, Standard, Division, Parent_Name, Address, Contact, Total, Average, class, result
from studentInformation
join marks
on studentInformation.student_id=marks.student_id;

alter table studentInformation change Name_of_the_student Name varchar(100);


select * from studentInformation;
select * from marks;
use school;
drop database school;
drop table marks;
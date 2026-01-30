show character set;

show databases;
create database logicfirst;
use logicfirst;
show tables;

create table student(
id int primary key,
name varchar(50),
gpa decimal(3,2)
);
describe student;
drop table student;
alter table student add department varchar(100);
alter table student drop department;

insert into student value
(21,"siva",7.3),
(16,"aswin",7.6);
insert into student(id,name) value(34,"sakthi");
select*from student;
select id,name from student;





create table employee(
Emp_id int,
Ename varchar(80),
JobDesc varchar(100),
Salary int
);

insert into employee value
(51,"Ram","Admin",1000000),
(52,"Harini","Manager",2500000),
(53,"George","Sales",2000000),
(54,"Ramya","sales",1300000),
(55,"Meena","HR",2000000),
(56,"Ashok","Manager",3000000),
(57,"Abdul","HR",2000000),
(58,"Ramya","Engineer",1000000),
(59,"Raghu","CEO",8000000),
(60,"Aravind","Manager",2800000),
(61,"Akshaya","Engineer",1000000),
(62,"John","Admin",2200000),
(63,"Abinaya","Engineer",2100000);

select Ename from employee where salary>2000000;
select * from employee where Ename="Ramya";
select * from employee where JobDesc = "Sales" or JobDesc = "Manager";
select * from employee where JobDesc in ("HR","CEO");
select * from employee where JobDesc not in ("HR","CEO");

select * from employee where Salary between 2000000 and 3000000
limit 5;

select * from employee where Ename like 'A%';

select * from employee where Ename not like 'A%';

select * from employee where Ename like 'A%a';

select * from employee where Ename like '%i%';

select * from employee where Ename like '__a%';

update employee set JobDesc = "Analyst" where JobDesc = "HR";

delete from employee where emp_id=59;

select * from employee
limit 5;

describe employee;







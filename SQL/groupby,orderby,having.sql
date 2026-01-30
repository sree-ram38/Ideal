create table student1(
student_name varchar(100),
mark int,
department varchar(100)
);

insert into student1 value
("Bharath",67,"CSE"),
("Venkat",89,"ECE"),
("Praveen",23,"MECH"),
("Abdul",63,"CSE"),
("Kadhir",88,"CSE"),
("John",81,"MECH"),
("Manoj",91,"CSE"),
("Mani",50,"ECE");
select * from student1 where department="CSE";
select student_name,mark from student1;
select student_name,mark from student1 order by mark desc;
select student_name,mark from student1 order by mark asc;
select avg(mark) from student1 group by department;
select count(student_name)as name,department from student1 group by department;
select count(student_name)as name,department from student1 group by department order by name asc;
select * from student1;



create table employee(
EmployeeId int,
FirstName varchar(50),
LastName varchar(50),
Department varchar(50),
salary int
);

insert into employee(EmployeeId,FirstName,LastName,Department,salary)
value
(1,"John","Doe","HR",55000),
(2,"Jane","Smith","IT",60000),
(3,"Bob","Johnson","IT",62000),
(4,"Alice","Williams","HR",54000),
(5,"Eva","Davis","Finance",58000),
(6,"Mike","Brown","Finance",59000);
select * from employee order by LastName asc ;
select * from employee where Department="IT" order by salary desc;
select count(*) from employee group by Department;
select count(*),Department from employee group by Department;
select count(*) from employee where Department="HR";
select * from employee group by department;
select * from employee where Department="IT";
select salary,Department from employee;
select avg(salary) as TotalSalary,Department from employee group by Department order by Department asc;
select avg(salary) as TotalSalary,Department from employee group by Department order by TotalSalary desc limit 1;
select avg(salary),Department from employee group by Department order by Department desc;
select avg(salary),Department from employee group by Department having avg(salary) <60000 order by Department desc;
select COUNT(*) AS employee_count,Department,avg(salary) AS avgSalary from employee group by Department having avg(salary) > 55000;




select * from employee;

create table student(
student_name varchar(100),
student_mark varchar(100),
department varchar(100)
);

alter table student change student_mark student_mark int;

insert into student value
("sree",1,"B.Sc CS"),
("siva",2,"B.Tech(IT)"),
("gokul",1,"B.E Eng"),
("kumar",3,"Mech"),
("aswin",2,"CSE"); 
select sum(student_mark) from student;
select sum(student_mark) as total_marks from student;
select max(student_mark) from student;
select min(student_mark) from student;
select avg(student_mark) from student;
select count(department) from student where department="CSE";
select count(student_name) from student;

select * from student;

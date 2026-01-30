create table student1(
name varchar(30),
age int,
department varchar(50)
)

insert into student1 value("john",19,"B.Tech(IT)")
insert into student1 value("Bharathi",20,"Data science"),("Bhuvanesh",19,"B.Tech(ECE)");
update student1 set department="DS" where department="Data science"
update student1 set age=20 where age=19
update student1 set age=18 where name="john"

--this is used to view the table
select * from student1 










create table fruit(
name varchar(40),
price varchar(40)
)

insert into fruit value("Apple","100"),("Grape","60"),("Banana","20");
delete from fruit where name="Apple"
delete from fruit
select * from fruit
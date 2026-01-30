use logicfirst;


select distinct JobDesc from employee;
select * from employee order by Salary desc;
select * from employee order by JobDesc,Ename;
select * from employee where JobDesc = "Manager" order by Ename;
select * from employee order by (case JobDesc
when 'Sales' then 1
when 'Admin' then 2
when 'Manager' then 3
when 'HR' then 4
when 'CEO' then 5
else 50 end
);  

select * from employee order by (case JobDesc
when 'Sales' then 1
when 'Admin' then 2
when 'Manager' then 3
when 'HR' then 4
else 50 end
),Ename;

select count(*) from employee;
select count(*) as Total_Manager from employee where JobDesc = 'Manager';
select avg(Salary) from employee where JobDesc = 'Manager';
select sum(Salary) from employee where JobDesc = 'Admin';
select max(Salary) from employee where JobDesc = 'Admin';
select max(Salary) from employee;
select ucase(Ename),Salary from employee;
select lcase(Ename) as Name,Salary from employee;
select Ename,char_length(Ename) as Length from employee;
select Ename,concat("Mr.",Ename) as NAME from employee;
select Ename,format(Salary,0) as SALARY from employee;
select Ename,left(JobDesc,4) as Length from employee;
select Ename,right(JobDesc,4) as Length from employee;
select Ename,reverse(JobDesc) as Reverse from employee;

alter table employee add column Hired_Date date;
update employee set Hired_Date="2025-12-08";

update employee set Hired_Date = "2025-11-23" where JobDesc = "CEO";

select now();
select date(now());
select curdate();
select date_format(curdate(),"%d/%m/%y") as date;
select datediff(curdate(),"2024/12/12");
select date_add(curdate(),interval 3 year ) as tomorrow;

select JobDesc,count(Ename) from employee group by JobDesc;
















select * from employee;

drop table employee;

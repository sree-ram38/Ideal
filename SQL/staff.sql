create table customer(
customer_id int,
customer_name varchar(50),
customer_address varchar(100),
city varchar(50),
state varchar(50),
zip_code varchar(60)
);

insert into customer value 
(1,"john Doe","392 sunset Blvd","New York","NT","10059","555-123-4567"),
(2,"Mary Smith","6900 Main St.","San Francisco","CA","94032","555-987-6543"),
(3,"Richard Newman","2040 Riverside Rd.","San Diego","CA","92010","555-555-5555"),
(4,"Cathy Cook","4010 speedway","San Diego","CA","85719","555-321-7890"),
(5,"Alice Johnson","123 Oak Street","San Diego","CA","90001","555-111-2222"),
(6,"Bob Williams","456 Elm Avenue","Chicago","IL","60601","555-444-7777");
alter table customer add column mobile_number varchar(20);
alter table customer change customer_address address varchar(100);
delete from customer where mobile_number is null;
delete from customer where zip_code="60601";
update customer set mobile_number="82206-1234" where mobile_number="555-987-6543";
drop table customer;
select * from customer;
select customer_name from customer;
select customer_name from customer where state="CA";
select * from customer where customer_id>2;
alter table customer drop column mobile_number;
truncate table customer;







create table customer1(
customer_id varchar(50),
customer_name varchar(50),
customer_address varchar(50),
city varchar(50),
state varchar(50),
zip_code varchar(50));

insert into customer1 value 
(1,"john Doe","392 sunset Blvd","New York","NT","10059"),
(2,"Mary Smith","6900 Main St.","San Francisco","CA","94032"),
(3,"Richard Newman","2040 Riverside Rd.","San Diego","CA","92010"),
(4,"Cathy Cook","4010 speedway","Tucson","AZ","85719");

alter table customer1 change column customer_address address varchar(100);
alter table customer1 add column mobile_number varchar(20);
delete from customer1 where mobile_number is null;

insert into customer1 value 
(1,"john Doe","392 sunset Blvd","New York","NT","10059","555-123-4567"),
(2,"Mary Smith","6900 Main St.","San Francisco","CA","94032","555-987-6543"),
(3,"Richard Newman","2040 Riverside Rd.","San Diego","CA","92010","555-555-5555"),
(4,"Cathy Cook","4010 speedway","San Diego","CA","85719","555-321-7890"),
(5,"Alice Johnson","123 Oak Street","San Diego","CA","90001","555-111-2222"),
(6,"Bob Williams","456 Elm Avenue","Chicago","IL","60601","555-444-7777");
update customer1 set mobile_number="82206-1234" where customer_name="Mary Smith";
delete from customer1 where zip_code="60601";
select * from customer1 where state="CA";
select customer_name from customer1 where state="CA";
select address from customer1 where state="CA";
select * from customer1 where customer_id>2;
alter table customer1 drop column mobile_number;
truncate customer1;
select * from customer1;
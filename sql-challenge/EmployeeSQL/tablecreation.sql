-- https://app.quickdatabasediagrams.com/#/d/1xqGnd
create table titles(
	title_id varchar(30) not null primary key,
	title varchar(30) not null
);
create table salaries(
	emp_no int primary key,
	salary int,
	foreign key (emp_no) references employees(emp_no)
);
create table employees(
	emp_no int primary key,
	emp_title varchar(30) not null,
	birth_date varchar(30) not null,
	first_name varchar(30) not null,
	last_name varchar(30) not null,
	sex varchar(30) not null,
	hire_date varchar(30) not null,
	foreign key (emp_title) references titles(title_id)
);
create table dept_manager(
	dept_no varchar(30) not null,
	emp_no int primary key,
	foreign key (emp_no) references employees(emp_no),
	foreign key(dept_no) references departments(dept_no)
);
create table dept_emp(
	emp_no int,
	dept_no varchar(30) not null,
	foreign key (emp_no) references employees(emp_no),
	foreign key (dept_no) references departments(dept_no)
);
create table departments(
	dept_no varchar(30) not null primary key,
	dept_name varchar(30) not null
);

select * from departments;
select * from dept_emp;
select * from dept_manager;
select * from employees;
select * from salaries;
select * from titles;

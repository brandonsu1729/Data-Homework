-- 1 List the following details of each employee: employee number, first name, last name, gender, and salary
select employees.emp_no, last_name, first_name, sex, salaries.salary from employees
join salaries 
on employees.emp_no = salaries.emp_no;

-- 2 List employees who were hired in 1986.
select *  from employees
where hire_date like '%1996';

-- 3 List the manager of each department with the following information: department number, 
-- department name, the manager's employee number, first name, last name, and start 
-- and end employment dates. (???)

select departments.dept_no, departments.dept_name, employees.emp_no, employees.first_name, employees.last_name, employees.hire_date from departments
join dept_manager
on dept_manager.dept_no = departments.dept_no
join employees
on dept_manager.emp_no = employees.emp_no;

-- 4 List the department of each employee with the following information: employee number, first name, last name, and department name.
select employees.emp_no, employees.first_name, employees.last_name, departments.dept_name from employees
join dept_emp
on dept_emp.emp_no = employees.emp_no
join departments
on departments.dept_no = dept_emp.dept_no;

-- 5 List all employees whose first name is "Hercules" and last names begin with "B."
select * from employees
where first_name = 'Hercules' and last_name like 'B%';

-- 6 List all employees in the Sales department, including their employee number, first name, last name, and department name.
select employees.emp_no, employees.first_name, employees.last_name, departments.dept_name from employees
join dept_emp
on dept_emp.emp_no = employees.emp_no
join departments
on departments.dept_no = dept_emp.dept_no
where departments.dept_name = 'Sales';

-- 7 List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name
select employees.emp_no, employees.first_name, employees.last_name, departments.dept_name from employees
join dept_emp
on dept_emp.emp_no = employees.emp_no
join departments
on departments.dept_no = dept_emp.dept_no
where departments.dept_name = 'Sales' or departments.dept_name = 'Development';

-- 8 In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name, count(last_name) from employees
group by last_name
order by count desc;


select * from employees
where emp_no = '499942'
--dammit.

-- the ceil is necessary bc the question asks for the next biggest integer
select ceil(avg(salary)  - avg(cast(replace(cast(salary as char), '0','') as signed))) from employees;

-- you can shorten the above to this, i think it is because sql allows implicit casting when necessary
select ceil(avg(salary)  - avg(replace(salary, '0',''))) from employees;
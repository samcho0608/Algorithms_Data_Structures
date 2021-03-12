-- group by
-- group by basically groups rows with same value in the selected column

-- for instance,
--  count(*) from occupations group by occupation;
-- the above query groups those with same occupation
-- then counts how many values there are with that specific occupation      

select concat(name,'(',left(occupation,1),')') from occupations order by name;

select concat('There are a total of ', count(*), ' ', lower(occupation), 's.') 
from occupations group by occupation order by count(*), occupation;
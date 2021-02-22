-- case statement == switch in C++
-- case
--      when CONDITION then VALUE
--      ....
--      else ...
-- end
-- from TABLE

-- greatest and max are similar but different
-- max finds the max of a column
-- greatest finds the greatest value among the arguments
select case
when 2 * greatest(a,b,c) >= a+b+c then 'Not A Triangle'
when a=b and b=c then 'Equilateral'
when a=b or b=c or a=c then 'Isosceles'
else 'Scalene'
end
from triangles;
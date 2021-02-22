-- SQL ORDER BY
-- orders the selection in a desired order(based on columns)
-- by default, these orders are in ascending order.
-- when we have multiple orders,
-- first sorts the selection with the very first column,
-- if there are rows with same values in the first column, then it uses the next column
-- to order those that are same from previous column.

-- limit is basically head in linux

select city, length(city) from station order by length(city),city asc limit 1;
select city, length(city) from station order by length(city) desc, city asc limit 1;
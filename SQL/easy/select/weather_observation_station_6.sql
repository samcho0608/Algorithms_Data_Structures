--left(STR,N)
--gives N many characters from the string
select city from station where left(city,1)='a' or left(city,1)='e' or left(city,1)='i' or left(city,1)='o' or left(city,1)='u';
-- there's also right

-- or u can use the following
-- group items using ()? CHECK UP ON THIS
select city from station where left(city,1) in ('a','e','i','o','u');
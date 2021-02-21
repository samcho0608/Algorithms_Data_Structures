-- you can also use regex
select distinct(city) from station where city regexp '^[aeiou].*[aeiou]$'
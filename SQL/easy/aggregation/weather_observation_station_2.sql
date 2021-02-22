-- you can give 2nd argument to round function to
-- determine the decimal place you want to round the number to
select round(sum(lat_n), 2), round(sum(long_w),2) from station;
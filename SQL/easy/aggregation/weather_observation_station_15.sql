-- to use the result of another group function, you must use select FUNCTION from TABLE
-- () is a MUST
select round(long_w, 4) from station where lat_n = (select max(lat_n) from station where lat_n < 137.2345);
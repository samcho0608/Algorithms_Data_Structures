-- variables use @IDENTIFIER
-- cannot use variable in limit rigth away but one may do it using prepare and execute
-- if using subquery for from, alias is a must

select round(count(*) / 2) into @mid from station;
prepare query
    from 'select round(max(s.lat_n), 4) from (select lat_n from station order by lat_n limit ?) s';
    execute query using @mid;
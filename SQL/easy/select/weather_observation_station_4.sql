-- distinct gives the unique set
select count(city) - count(distinct(city)) from station;
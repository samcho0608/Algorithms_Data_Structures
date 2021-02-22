-- group by == for each basically
select continent, floor(avg(city.population)) from city join country on countrycode=code group by continent;
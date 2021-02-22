-- join basically finds the intersection btwn two tables based on condition after ON
-- if column present in both tables, specify using TABLE.COLUMN
select sum(city.population) from city join country on countrycode = code where continent='Asia';
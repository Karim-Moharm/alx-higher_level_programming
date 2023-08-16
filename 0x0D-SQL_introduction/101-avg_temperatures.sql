-- display average temperature by city orders by temperature (descending)
-- the date comming from temperatures.sql file

SELECT `city`, AVG(`value`) `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;

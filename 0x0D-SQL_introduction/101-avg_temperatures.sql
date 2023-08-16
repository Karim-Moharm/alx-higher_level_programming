-- display average temperature by city orders by temperature (descending)
-- the date comming from temp.sql file

SELECT `city`, AVG(`temperature`) `avg_temp`
FROM `temp`
GROUP BY `city`
ORDER BY `avg_temp` DESC;

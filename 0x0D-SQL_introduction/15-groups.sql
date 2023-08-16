-- list number of records with same score name in the table

SELECT `score`, COUNT(`score`) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `score` DESC;

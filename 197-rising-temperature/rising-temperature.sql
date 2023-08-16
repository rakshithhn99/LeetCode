# Write your MySQL query statement below

SELECT A.id FROM
Weather A INNER JOIN 
(SELECT DATE_ADD(recordDate, INTERVAL 1 DAY) as recordDate, temperature FROM Weather) B 
ON A.recordDate = B.recordDate
WHERE A.temperature > B.temperature;
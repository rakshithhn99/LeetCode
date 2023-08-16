# Write your MySQL query statement below

SELECT 
A.machine_id, 
ROUND(AVG(B.timestamp - A.timestamp), 3) as processing_time FROM
Activity A INNER JOIN Activity B
ON A.machine_id = B.machine_id
AND A.process_id = B.process_id
AND A.activity_type != B.activity_type
AND A.activity_type = 'start'
GROUP BY A.machine_id;
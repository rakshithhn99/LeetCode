# Write your MySQL query statement below

WITH CTE AS (
SELECT 
managerId, 
COUNT(*) AS numOfMang 
FROM Employee 
WHERE managerId IS NOT NULL
GROUP BY managerId
HAVING numOfMang >=5)

SELECT name 
FROM Employee INNER JOIN CTE 
ON Employee.id = CTE.managerId;

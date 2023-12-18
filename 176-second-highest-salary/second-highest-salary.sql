# Write your MySQL query statement below

WITH CTE AS (
    SELECT 
    SALARY, 
    DENSE_RANK() OVER(ORDER BY SALARY DESC) AS RN
    FROM Employee
)

SELECT
IFNULL((SELECT SALARY FROM CTE WHERE RN=2 LIMIT 1), NULL) AS SecondHighestSalary;
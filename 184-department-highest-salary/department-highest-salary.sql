# Write your MySQL query statement below

WITH CTE AS 
(SELECT 
Dept.name as Department,
Emp.name as Employee,
salary as Salary
FROM 
Employee Emp
INNER JOIN
Department Dept
ON Emp.departmentId = Dept.id) 


SELECT 
Department,
Employee,
Salary
FROM (SELECT
Department,
Employee,
Salary, 
RANK() OVER(PARTITION BY Department ORDER BY Salary DESC) AS RN
FROM CTE) Temp Where Temp.RN = 1;




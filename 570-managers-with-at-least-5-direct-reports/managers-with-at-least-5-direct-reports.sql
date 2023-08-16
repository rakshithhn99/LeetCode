# Write your MySQL query statement below

SELECT T.name FROM (
SELECT A.id, A.name, COUNT(A.id) as reportcount FROM 
Employee A INNER JOIN Employee B
ON A.id = B.managerId
GROUP BY
A.id,
A.name ) T
WHERE T.reportcount >= 5;


/* Explanation : 
Since input is only one table Employee table that has both employee and manager Id details. 

We should treat same table as employee and manager perspective. So join id with managerId. 

Here while selecting either we can select A.id or B.managerId but selecting name we should select left table name since right table name keep on changes(employee name). 
Rest is self explanatory..
*/
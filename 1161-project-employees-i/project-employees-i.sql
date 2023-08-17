# Write your MySQL query statement below
SELECT project_id,
ROUND(AVG(experience_years), 2) as average_years
FROM Project A INNER JOIN Employee B
ON A.employee_id = B.employee_id
GROUP BY project_id;
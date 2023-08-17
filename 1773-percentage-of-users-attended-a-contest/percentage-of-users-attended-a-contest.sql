# Write your MySQL query statement below


SELECT contest_id,
ROUND((COUNT(A.user_id)/(SELECT COUNT(*) FROM Users) * 100), 2) AS percentage
FROM 
Users A INNER JOIN Register B
ON A.user_id = B.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
# Write your MySQL query statement below
SELECT query_name,
ROUND(SUM((rating / position)) / COUNT(query_name), 2) as quality,
ROUND((COUNT(IF(rating < 3, 1, NULL)) / COUNT(query_name)) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
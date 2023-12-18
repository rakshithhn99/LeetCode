# Write your MySQL query statement below

WITH CTE AS
(SELECT
SCORE,
DENSE_RANK() OVER(ORDER BY SCORE DESC) AS RN
FROM Scores)

SELECT
ROUND(SCORE, 2) AS score,
RN as "rank"
FROM CTE;

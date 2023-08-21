# Write your MySQL query statement below
SELECT 
ROUND(COUNT(A.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM
(SELECT
player_id,
MIN(event_date) as first_login
FROM
Activity
GROUP BY
player_id
HAVING (player_id, DATE_ADD(first_login, INTERVAL 1 DAY)) IN 
  (SELECT player_id, event_date FROM Activity)
) A;
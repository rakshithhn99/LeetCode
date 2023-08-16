SELECT A.user_id,
ROUND(AVG(IF(B.action = 'confirmed', 1.0, 0)),2) as confirmation_rate
FROM 
Signups A LEFT JOIN Confirmations B
ON A.user_id = B.user_id
GROUP BY 
A.user_id;
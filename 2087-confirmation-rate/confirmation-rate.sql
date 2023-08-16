SELECT 
user_id,
CASE WHEN
total_requests = 0 THEN 0.00
ELSE ROUND(confirmed_requests/total_requests, 2)
END AS confirmation_rate
FROM
  (SELECT 
  A.user_id,
  A.confirmed_requests,
  IFNULL(B.total_requests, 0) AS total_requests
  FROM 
    (SELECT 
    A.user_id, 
    IFNULL(confirmed_requests, 0) as confirmed_requests
    FROM Signups A
    LEFT JOIN 
    (SELECT user_id, COUNT(action) AS confirmed_requests 
    FROM Confirmations 
    WHERE action = 'confirmed'
    GROUP BY
    user_id) B
    ON A.user_id = B.user_id) A

    LEFT JOIN 

    (SELECT user_id, COUNT(action)AS total_requests 
    FROM Confirmations 
    GROUP BY
    user_id) B

  ON A.user_id = B.user_id
) T;
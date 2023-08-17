# Write your MySQL query statement below

SELECT 
A.product_id,
ROUND((SUM((price * units)) / SUM(units)), 2) as average_price
FROM Prices A INNER JOIN UnitsSold B
ON A.product_id = B.product_id
AND B.purchase_date BETWEEN A.start_date AND A.end_date
GROUP BY A.product_id;


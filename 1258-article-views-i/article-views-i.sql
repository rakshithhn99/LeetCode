# Write your MySQL query statement below

# Inner Query

SELECT DISTINCT author_id AS id FROM Views 
WHERE author_id = viewer_id
ORDER BY author_id;

/* Using Join --

SELECT DISTINCT A.author_id as id FROM 
Views A INNER JOIN Views B
ON A.author_id = B.viewer_id
ORDER BY A.author_id; */
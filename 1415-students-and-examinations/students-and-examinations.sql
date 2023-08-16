# Write your MySQL query statement below

SELECT 
A.student_id, 
A.student_name, 
A.subject_name, 
COUNT(B.subject_name) AS attended_exams 
FROM
(SELECT * FROM Students CROSS JOIN Subjects) A
LEFT JOIN Examinations B
ON A.student_id = B.student_id
AND A.subject_name = B.subject_name
GROUP BY 
A.student_id, 
B.student_id, 
A.subject_name
ORDER BY 
A.student_id, A.subject_name;


/* Explanation : 

CROSS JOIN results in each student (id,name) with all subjects. Alice with Math, Physics and Ptogramming similarly all the subjects for for remaining students.

above output LEFT JOIN with Examination table results in all the records from above output and matched record from Examination. Examination.subject_name has NULL values for subject names which are not present in Examination table and it has subject_name for the mtched records. We need to result NULL value record count as 0 with mentioning subject name. */



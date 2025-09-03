-- CTE approach
WITH student_subject_combinations AS (
    SELECT S.student_id, 
        S.student_name, 
        SUB.subject_name
    FROM Students S
    CROSS JOIN Subjects AS SUB  
)
SELECT SSC.student_id, 
    SSC.student_name, 
    SSC.subject_name,
    COUNT(E.subject_name) AS attended_exams
FROM student_subject_combinations SSC
LEFT JOIN Examinations E 
    ON SSC.student_id = E.student_id 
    AND SSC.subject_name = E.subject_name
GROUP BY SSC.student_id, 
    SSC.student_name, 
    SSC.subject_name
ORDER BY SSC.student_id,
    SSC.Subject_name;
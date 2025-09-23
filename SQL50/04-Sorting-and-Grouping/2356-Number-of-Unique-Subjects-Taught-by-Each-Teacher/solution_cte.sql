-- CTE approach
WITH teacher_unique_subjects AS (
    SELECT teacher_id, 
        COUNT(DISTINCT subject_id) AS cnt
    FROM Teacher
    GROUP BY teacher_id
)
SELECT teacher_id, 
    cnt
FROM teacher_unique_subjects;
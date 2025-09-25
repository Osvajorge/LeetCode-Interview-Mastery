-- CTE approach
WITH at_least_five_students AS (
    SELECT class 
    FROM Courses 
    GROUP BY class 
    HAVING COUNT(student) >= 5
)
SELECT class FROM at_least_five_students;
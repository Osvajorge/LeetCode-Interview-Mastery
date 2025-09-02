-- CTE approach
WITH employee_bonus AS (
    SELECT e.name,
        b.bonus
    FROM Employee e
    LEFT JOIN Bonus b ON e.empId = b.empId
    WHERE b.
    bonus < 1000 or b.bonus IS NULL
)
SELECT name,
    bonus
FROM employee_bonus;
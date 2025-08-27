-- CTE approach
WITH employee_mapping AS (
    SELECT e.id, e.name, eu.unique_id
    FROM Employees e
    LEFT JOIN EmployeeUNI eu ON e.id = eu.id
)
SELECT unique_id, name FROM employee_mapping;


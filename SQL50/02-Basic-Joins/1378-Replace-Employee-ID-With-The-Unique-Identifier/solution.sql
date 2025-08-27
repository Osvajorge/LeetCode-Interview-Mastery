-- Add your SQL solution here
SELECT eu.unique_id,
    e.name 
FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id;  
-- CTE approach
WITH manager_report AS (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)
SELECT e.name
FROM manager_report m 
INNER JOIN Employee e ON m.managerId = e.id;
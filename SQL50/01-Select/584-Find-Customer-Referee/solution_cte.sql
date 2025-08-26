-- CTE approach
WITH refered_customers AS (
    SELECT name
    FROM Customer 
    WHERE referee_id != 2 OR referee_id IS NULL
)
SELECT name FROM refered_customers
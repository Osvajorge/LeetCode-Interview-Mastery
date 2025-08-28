-- CTE approach
WITH temperature_comparison AS (
    SELECT w1.id,
           w1.temperature as current_temp,
           w2.temperature as previous_temp
    FROM Weather w1
    INNER JOIN Weather w2 ON w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
)
SELECT id
FROM temperature_comparison
WHERE current_temp > previous_temp;
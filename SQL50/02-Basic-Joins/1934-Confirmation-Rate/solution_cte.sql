-- CTE approach
WITH confirmed_actions AS (
    SELECT user_id,
    ROUND(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END)/
    COUNT(CASE WHEN action THEN 1 ELSE 0 END),2) AS confirmation_rate
    FROM Confirmations
    GROUP BY user_id
)
SELECT s.user_id,
    COALESCE(ca.confirmation_rate, 0.00) AS confirmation_rate 
FROM Signups s
LEFT JOIN confirmed_actions ca ON s.user_id = ca.user_id;
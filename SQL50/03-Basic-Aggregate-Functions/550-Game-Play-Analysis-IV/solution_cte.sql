-- CTE approach
WITH first_logins AS (
    SELECT 
        player_id,
        MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),
day_after_first AS (
    -- Find all logins that happened exactly one day after first login
    SELECT a.player_id
    FROM Activity a
    JOIN first_logins f ON a.player_id = f.player_id 
                        AND a.event_date = f.first_login_date + INTERVAL 1 DAY
)
SELECT 
    ROUND(
        COUNT(DISTINCT daf.player_id) * 1.0 / COUNT(DISTINCT fl.player_id), 
        2
    ) AS fraction
FROM first_logins fl
LEFT JOIN day_after_first daf ON fl.player_id = daf.player_id;
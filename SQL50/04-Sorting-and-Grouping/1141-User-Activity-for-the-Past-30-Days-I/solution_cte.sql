-- CTE approach
WITH daily_active_users AS (
    SELECT activity_date as day,
        COUNT(DISTINCT user_id) AS active_users
    FROM activity activity_date
    WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
    GROUP BY activity_date
)
SELECT day,
    active_users
FROM daily_active_users;
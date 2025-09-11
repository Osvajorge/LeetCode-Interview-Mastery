WITH attended_contest_percentage AS (
    SELECT
        r.contest_id,
        ROUND(COUNT(r.user_id) / (SELECT COUNT(*) FROM users) * 100,2) AS percentage
    FROM Register r  
    INNER JOIN users u ON u.user_id = r.user_id
    GROUP BY r.contest_id
    ORDER BY percentage DESC, contest_id ASC 
) 
SELECT contest_id,
    percentage
FROM attended_contest_percentage;
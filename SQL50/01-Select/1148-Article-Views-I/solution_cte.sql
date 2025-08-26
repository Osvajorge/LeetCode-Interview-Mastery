-- CTE approach
WITH self_viewers AS (
    SELECT DISTINCT author_id
    FROM Views
    WHERE viewer_id = author_id
)
SELECT author_id AS id
FROM self_viewers
ORDER BY author_id;
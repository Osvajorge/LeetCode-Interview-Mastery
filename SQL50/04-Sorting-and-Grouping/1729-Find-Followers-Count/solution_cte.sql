-- CTE approach
WITH follower_counts AS (
    SELECT user_id, 
           COUNT(follower_id) AS followers_count
    FROM Followers
    GROUP BY user_id
)
SELECT user_id, 
       followers_count
FROM follower_counts
ORDER BY user_id;
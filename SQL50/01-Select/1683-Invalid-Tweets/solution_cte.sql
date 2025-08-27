-- CTE approach
WITH tweet_length AS (
    SELECT tweet_id 
    FROM Tweets
    WHERE LENGTH(content) > 15
)
SELECT tweet_id FROM tweet_length;
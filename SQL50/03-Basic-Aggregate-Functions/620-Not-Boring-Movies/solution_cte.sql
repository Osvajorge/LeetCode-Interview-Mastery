-- CTE approach
WITH filtered_movies AS (
    SELECT id, movie, description, rating
    FROM Cinema
    WHERE description != 'boring' AND id % 2 = 1
)
SELECT * FROM filtered_movies ORDER BY rating DESC;
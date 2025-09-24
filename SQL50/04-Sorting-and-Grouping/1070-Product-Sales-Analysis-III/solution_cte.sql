-- CTE approach
WITH first_year_sales AS (
    SELECT *,
        RANK() OVER (PARTITION BY product_id ORDER BY year) as rn
    FROM Sales
)
SELECT product_id,
    year AS first_year,
    quantity,
    price
FROM first_year_sales
WHERE rn = 1
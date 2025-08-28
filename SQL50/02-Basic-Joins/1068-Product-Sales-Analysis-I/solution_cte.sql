-- CTE approach
WITH product_report AS (
    SELECT p.product_name,
        s.year,
        s.price
    FROM Sales s
    LEFT JOIN Product p ON s.product_id  = p.product_id  
)
SELECT product_name,
    year,
    price
FROM product_report;
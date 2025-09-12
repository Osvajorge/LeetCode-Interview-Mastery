with monthly_transactions AS (
    SELECT 
        DATE_FORMAT(trans_date, '%Y-%m') AS month, 
        country,
        COUNT(id) AS trans_count,
        COUNT(CASE WHEN state = 'approved' THEN id END) AS approved_count,
        SUM(amount) AS trans_total_amount,
        SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
    FROM Transactions
    GROUP BY month, country
)
SELECT month, 
    country, 
    trans_count,
    approved_count,
    trans_total_amount,
    approved_total_amount
FROM monthly_transactions;
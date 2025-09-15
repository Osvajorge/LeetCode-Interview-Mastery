SELECT 
    ROUND(
        AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100, 
        2
    ) AS immediate_percentage
FROM (
    SELECT 
        order_date,
        customer_pref_delivery_date,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) as rn
    FROM Delivery
) ranked_orders
WHERE rn = 1;
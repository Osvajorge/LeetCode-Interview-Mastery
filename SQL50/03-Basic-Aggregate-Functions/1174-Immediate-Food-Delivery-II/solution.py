import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    first_orders = (delivery.sort_values('order_date')
                           .groupby('customer_id')
                           .first()
                           .reset_index())

    immediate_count = (first_orders['order_date'] == first_orders['customer_pref_delivery_date']).sum()
    total_customers = len(first_orders)
    immediate_percentage = round((immediate_count / total_customers) * 100, 2)

    return pd.DataFrame({'immediate_percentage': [immediate_percentage]})
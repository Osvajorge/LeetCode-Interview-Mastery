import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    refered_customers = customer[
        (customer['referee_id'] != 2) | 
        (customer['referee_id'].isnull())
        ]

    result = refered_customers[['name']]
    return result
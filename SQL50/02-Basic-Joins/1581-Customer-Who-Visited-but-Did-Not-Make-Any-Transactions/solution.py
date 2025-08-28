import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Find customers who visited but did not make any transactions.
    Returns customer_id and count of visits without transactions.
    """
    # LEFT JOIN to include all visits, even those without transactions
    merged_df = visits.merge(transactions, on='visit_id', how='left')
    
    # Filter visits without transactions (where transaction_id is null)
    no_transactions = merged_df[merged_df['transaction_id'].isnull()]
    
    # Group by customer_id and count visits without transactions
    result = (no_transactions.groupby('customer_id')
              .size()
              .reset_index(name='count_no_trans'))
    
    return result
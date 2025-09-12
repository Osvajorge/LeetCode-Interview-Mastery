import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:

    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')

    transactions['approved_amount'] = transactions['amount'].where(
        transactions['state'] == 'approved', 0
    )

    aggregation = transactions.groupby(['month', 'country'], dropna=False).agg({
        'id': 'count',
        'state': lambda x: (x == 'approved').sum(),
        'amount': 'sum',
        'approved_amount': 'sum'
    })
    
    result = aggregation.reset_index()

    result.columns = ['month', 'country', 'trans_count', 'approved_count', 
                      'trans_total_amount', 'approved_total_amount']
    
    return result
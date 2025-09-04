import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    #LEFT JOIN
    merged = signups.merge(confirmations, on='user_id', how='left')
    
    # GROUP BY + calculation 
    def calc_rate(group):
        confirmed = (group['action'] == 'confirmed').sum()
        total = group['action'].notna().sum()  # Count non-null actions
        return confirmed / total if total > 0 else 0.00
    
    result = (merged.groupby('user_id')
                    .apply(calc_rate)
                    .reset_index()
                    .rename(columns={0: 'confirmation_rate'}))
    
    #Round to 2 decimals
    result['confirmation_rate'] = result['confirmation_rate'].round(2)
    
    return result
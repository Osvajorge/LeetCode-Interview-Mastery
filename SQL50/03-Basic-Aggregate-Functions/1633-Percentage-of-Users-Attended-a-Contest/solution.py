import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    merged = register.merge(users, on='user_id', how='inner')

    result = merged.groupby('contest_id')['user_id'].nunique().reset_index()

    total_unique_users = users['user_id'].nunique()
    result['percentage'] = (result['user_id'] / total_unique_users * 100).round(2)

    result = result.sort_values(['percentage', 'contest_id'], ascending=[False, True])

    return result[['contest_id', 'percentage']]
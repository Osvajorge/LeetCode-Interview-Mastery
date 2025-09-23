import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:

    activity['activity_date'] = pd.to_datetime(activity['activity_date'])
    
    start_date = pd.to_datetime('2019-06-28')
    end_date = pd.to_datetime('2019-07-27')
    
    filtered_activity = activity[
        (activity['activity_date'] >= start_date) & 
        (activity['activity_date'] <= end_date)
    ]
    
    daily_active_users = (filtered_activity.groupby('activity_date')['user_id']
                         .nunique()
                         .reset_index()
                         .rename(columns={'activity_date': 'day', 'user_id': 'active_users'}))
    
    return daily_active_users
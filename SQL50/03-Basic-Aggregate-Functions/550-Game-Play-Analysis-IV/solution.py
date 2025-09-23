import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Find each player's first login date
    first_logins = activity.groupby('player_id')['event_date'].min().reset_index()
    first_logins.columns = ['player_id', 'first_login_date']
    
    # Step 2: Create the expected "day 2" date for each player
    first_logins['expected_day2'] = first_logins['first_login_date'] + pd.Timedelta(days=1)
    
    # Step 3: Check which players actually logged in on their expected day 2
    # Merge to see if there's a matching login
    day2_check = activity.merge(
        first_logins[['player_id', 'expected_day2']], 
        on='player_id'
    )
    
    # Filter for actual logins on expected day 2
    retained_players = day2_check[
        day2_check['event_date'] == day2_check['expected_day2']
    ]['player_id'].nunique()
    
    # Step 4: Calculate fraction
    total_players = activity['player_id'].nunique()
    fraction = round(retained_players / total_players, 2)
    
    return pd.DataFrame({'fraction': [fraction]})
import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    follower_counts = (
        followers
        .groupby('user_id')['follower_id']
        .count()
        .reset_index(name='followers_count')
        .sort_values(by='user_id')
        )

    return follower_counts
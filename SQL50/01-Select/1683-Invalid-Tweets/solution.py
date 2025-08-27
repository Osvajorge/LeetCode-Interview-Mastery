import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweet_length_df = tweets[
        (tweets['content'].str.len()> 15)
    ]
    result_df = tweet_length_df[['tweet_id']]
    return result_df

# One-liner with method chaining (more pythonic)
#return tweets[tweets['content'].str.len() > 15][['tweet_id']]
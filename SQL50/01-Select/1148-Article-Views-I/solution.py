import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    # Step 1: Filter the DataFrame to find self-viewers. The parentheses are crucial for correct operator precedence.
    self_viewers_df = views[
        (views['viewer_id'] == views['author_id'])
        ]
    # Step 2: Get the unique author IDs from the filtered DataFrame. The .unique() method returns a NumPy array of unique values,
    # which it needs to be converted into a Pandas Series for sorting.
    unique_authors = self_viewers_df['author_id'].unique()
    
    # Step 3: Sort the unique author IDs. Converting the NumPy array to a Pandas Series allows us to use the .sort_values() method.
    sorted_authors = pd.Series(unique_authors).sort_values()
    
    # Step 4: Convert the sorted Series into a DataFrame with the required column name 'id'.
    result_df = pd.DataFrame(sorted_authors, columns=['id'])
    
    return result_df


###
# return (views[views['viewer_id'] == views['author_id']]
#             ['author_id']
#             .drop_duplicates()
#             .sort_values()
#             .to_frame(name='id')
#             .reset_index(drop=True))
###
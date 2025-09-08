import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    not_boring_odd_movies = cinema[(cinema['id'] % 2 == 1) 
        & (cinema['description'] != 'boring')]

    result = not_boring_odd_movies.sort_values(by='rating', ascending=False)
    return result
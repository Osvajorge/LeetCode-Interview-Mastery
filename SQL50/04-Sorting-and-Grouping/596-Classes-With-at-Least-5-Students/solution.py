import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    
    group_count = courses.groupby('class')['student'].count()
    
    result = group_count[group_count >= 5].reset_index()[['class']]

    return result
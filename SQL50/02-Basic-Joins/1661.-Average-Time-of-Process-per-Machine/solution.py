import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    a1 = activity[activity['activity_type'] == 'start']
    a2 = activity[activity['activity_type'] == 'end']
    

    merged = a1.merge(
        a2, 
        on=['machine_id', 'process_id'],  
        suffixes=('_start', '_end')
    )

    merged['processing_time'] = merged['timestamp_end'] - merged['timestamp_start']

    result = merged.groupby('machine_id')['processing_time'].mean().round(3).reset_index()

    return result
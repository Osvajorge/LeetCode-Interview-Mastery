import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:

    weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    merged = weather.merge(
        weather,
        left_on=weather['recordDate'] - pd.Timedelta(days=1),  
        right_on='recordDate',
        suffixes=('', '_prev')                               
    )

    result = merged[merged['temperature'] > merged['temperature_prev']]

    return result[['id']]
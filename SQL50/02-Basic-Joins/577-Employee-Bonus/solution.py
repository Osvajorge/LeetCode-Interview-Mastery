import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(bonus, on='empId', how='left')

    bonus_df = merged_df[(merged_df['bonus'] < 1000) | (merged_df['bonus'].isna())]

    result_df = bonus_df[['name', 'bonus']]

    return result_df
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = project.merge(employee, on='employee_id', how='inner')

    result = merged_df.groupby(by='project_id')[['experience_years']].mean().round(2).reset_index()

    result.columns = ['project_id', 'average_years']

    return result
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_counts = employee.groupby('managerId').size()

    report_counts = report_counts[report_counts >= 5].index

    result = employee[employee['id'].isin(report_counts)][['name']]

    return result
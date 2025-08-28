import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged_df = sales.merge(product, on='product_id', how='left')

    result_df = merged_df[['product_name', 'year', 'price']]

    return result_df
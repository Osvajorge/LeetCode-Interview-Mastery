import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    df_ranked = sales.assign(
        rn=sales.groupby('product_id')['year'].rank(method='dense')
    )

    result = df_ranked[df_ranked['rn'] == 1][
        ['product_id', 'year', 'quantity', 'price']
    ].rename(columns={'year': 'first_year'})

    return result
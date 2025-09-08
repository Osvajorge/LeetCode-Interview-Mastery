def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    merged = prices.merge(units_sold, on='product_id', how='left')
    
    # NO filtrar aquí - mantener todos los productos
    merged['valid_sale'] = (
        (merged['purchase_date'] >= merged['start_date']) & 
        (merged['purchase_date'] <= merged['end_date'])
    )
    
    def calculate_avg(group):
        valid_rows = group[group['valid_sale'] == True]
        if len(valid_rows) == 0 or valid_rows['units'].sum() == 0:
            return 0
        return (valid_rows['price'] * valid_rows['units']).sum() / valid_rows['units'].sum()
    
    result = merged.groupby('product_id').apply(calculate_avg).round(2)
    return result.reset_index(name='average_price')
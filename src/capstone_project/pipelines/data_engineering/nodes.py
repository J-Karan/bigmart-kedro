"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.7
"""
import pandas as pd

def calculate_quantity_sold(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Quantity Sold based on Item Outlet Sales and Item MRP.

    Args:
        df (pd.DataFrame): Input DataFrame containing 'Item_Outlet_Sales' and 'Item_MRP'.

    Returns:
        pd.DataFrame: DataFrame with an additional 'Quantity_Sold' column.
    """
    df['Quantity_Sold'] = df['Item_Outlet_Sales'] / df['Item_MRP']
    df['Quantity_Sold'] = df['Quantity_Sold'].astype('int64')
    return df

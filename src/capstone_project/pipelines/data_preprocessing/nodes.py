"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.19.7
"""

import pandas as pd
from typing import Optional


def add_primary_key(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a primary key column to the DataFrame by combining 'Outlet_Identifier' and 'Item_Identifier'.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with the new 'primary key' column.
    """
    df["primary key"] = df["Outlet_Identifier"] + df["Item_Identifier"]
    return df


def fill_missing_weights(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fills missing 'Item_Weight' values with the mode weight for the corresponding 'Item_Identifier'.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with missing 'Item_Weight' values filled.
    """
    if df.empty:
        return df

    nulls = df[df["Item_Weight"].isnull()]["Item_Identifier"].unique()
    for item in nulls:
        mode_weight = df[df["Item_Identifier"] == item]["Item_Weight"].mode()
        if not mode_weight.empty:
            df.loc[
                (df["Item_Identifier"] == item) & (df["Item_Weight"].isna()),
                "Item_Weight",
            ] = mode_weight[0]

    return df


def fill_missing_outletsize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fills missing values in a specified column with a default value.

    Args:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the column to fill.
        default_value (str): The value to fill missing entries with. Default is "Small".

    Returns:
        pd.DataFrame: The DataFrame with missing values in the specified column filled.
    """
    df["Outlet_Size"] = df["Outlet_Size"].fillna("Small")
    return df


def fill_visibility_with_mean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fills missing 'Item_Visibility' values with the mean visibility of the corresponding 'Item_Type'.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with missing 'Item_Visibility' values filled.
    """
    if df.empty:
        return df

    item_types_with_zero_visibility = df[df["Item_Visibility"] == 0][
        "Item_Type"
    ].unique()
    for item_type in item_types_with_zero_visibility:
        visibility_mean = df[df["Item_Type"] == item_type]["Item_Visibility"].mean()
        df.loc[
            (df["Item_Type"] == item_type) & (df["Item_Visibility"] == 0),
            "Item_Visibility",
        ] = visibility_mean

    return df


def normalize_fat_content(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizes 'Item_Fat_Content' values to a standard format.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with normalized 'Item_Fat_Content' values.
    """
    df["Item_Fat_Content"] = df["Item_Fat_Content"].map(
        {"Low Fat": "LF", "low fat": "LF", "Regular": "reg", "LF": "LF", "reg": "reg"}
    )
    return df


def pre_process_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies a sequence of preprocessing steps to the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with preprocessing applied.
    """
    df = add_primary_key(df)
    df = fill_missing_weights(df)
    df = fill_missing_outletsize(df)
    df = fill_visibility_with_mean(df)
    df = normalize_fat_content(df)
    return df

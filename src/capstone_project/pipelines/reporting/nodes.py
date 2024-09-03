"""
This is a boilerplate pipeline 'reporting'
generated using Kedro 0.19.7
"""

import pandas as pd
import plotly.express as ex
import plotly.graph_objs as go
import statsmodels.api as sm


def create_item_visibility_box_plot_by_outlet_type(df: pd.DataFrame):
    fig = go.Figure()

    # Add a box trace for each outlet type
    for outlet_type in df["Outlet_Type"].unique():
        fig.add_trace(
            go.Box(
                y=df[df["Outlet_Type"] == outlet_type]["Item_Visibility"],
                name=outlet_type,
            )
        )

    # Update layout with titles
    fig.update_layout(
        title="Box plot of Item Visibility",
        xaxis_title="Outlet Type",
        yaxis_title="Item Visibility",
    )

    return fig


def create_mrp_sales_scatter_plot(df: pd.DataFrame):
    per_item_sale = (
        df.groupby("Item_Identifier")["Item_Outlet_Sales"].sum().reset_index()
    )
    per_item_mrp = df.groupby("Item_Identifier")["Item_MRP"].mean().reset_index()
    mrp_sales_comparison_data = pd.concat([per_item_sale, per_item_mrp], axis=1)

    x = mrp_sales_comparison_data["Item_MRP"]
    y = mrp_sales_comparison_data["Item_Outlet_Sales"]

    scatter_trace = go.Scatter(
        x=x, y=y, mode="markers", marker=dict(color="orange"), name="Data"
    )

    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    predictions = model.predict(X)

    trendline_trace = go.Scatter(
        x=x, y=predictions, mode="lines", line=dict(color="white"), name="Trendline"
    )

    fig = go.Figure()

    fig.add_trace(scatter_trace)
    fig.add_trace(trendline_trace)

    fig.update_layout(
        title="Revenue Generated vs Item MRP",
        xaxis_title="Item MRP",
        yaxis_title="Revenue Generated",
    )

    return fig


def create_mrp_quantity_scatter_plot(df: pd.DataFrame):
    avg_item_mrp = df.groupby(["Item_Identifier"])["Item_MRP"].mean().reset_index()
    per_item_qty_sold = (
        df.groupby(["Item_Identifier"])["Quantity_Sold"].sum().reset_index()
    )
    item_mrp_qty_comp = pd.concat([avg_item_mrp, per_item_qty_sold], axis=1)

    x = item_mrp_qty_comp["Item_MRP"]
    y = item_mrp_qty_comp["Quantity_Sold"]

    scatter_trace = go.Scatter(
        x=x, y=y, mode="markers", marker=dict(color="orange"), name="Data"
    )

    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    predictions = model.predict(X)

    trendline_trace = go.Scatter(
        x=x, y=predictions, mode="lines", line=dict(color="white"), name="Trendline"
    )

    fig = go.Figure()

    fig.add_trace(scatter_trace)
    fig.add_trace(trendline_trace)

    fig.update_layout(
        title="Qunatity Sold vs Item MRP",
        xaxis_title="Item MRP",
        yaxis_title="Quantity_Sold",
    )

    return fig


def create_average_revenue_by_product(df: pd.DataFrame):
    fat_content_sales = (
        df.groupby("Item_Fat_Content")["Item_Outlet_Sales"].median().reset_index()
    )
    return fat_content_sales

"""
This is a boilerplate pipeline 'reporting'
generated using Kedro 0.19.7
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import (
    create_item_visibility_box_plot_by_outlet_type,
    create_mrp_sales_scatter_plot,
    create_mrp_quantity_scatter_plot,
    create_average_revenue_by_product,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_item_visibility_box_plot_by_outlet_type,
                inputs="final_preprocessed_data",
                outputs="item_visiblitity_box_plot",
            ),
            node(
                func=create_mrp_sales_scatter_plot,
                inputs="final_preprocessed_data",
                outputs="mrp_sales_scatter_plot",
            ),
            node(
                func=create_mrp_quantity_scatter_plot,
                inputs="main_dataset_cleaned",
                outputs="mrp_quantity_scatter_plot",
            ),
            node(
                func=create_average_revenue_by_product,
                inputs="main_dataset_cleaned",
                outputs="average_revenue_by_product",
            ),
        ]
    )

"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.7
"""

# src/<your_project>/pipelines/data_processing/pipeline.py

from kedro.pipeline import Pipeline, node
from .nodes import calculate_quantity_sold

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=calculate_quantity_sold,
                inputs="final_preprocessed_data",  
                outputs="main_dataset_cleaned",
                name="calculate_quantity_sold_node",
            ),
        ]
    )

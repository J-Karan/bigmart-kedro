from kedro.pipeline import Pipeline, node
from .nodes import pre_process_data


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=pre_process_data,
                inputs="mart",
                outputs="final_preprocessed_data",
                name="pre_processed_node",
            ),
        ]
    )

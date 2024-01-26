"""
This is a boilerplate pipeline 'data_split'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data_for_evaluation


def create_pipeline() -> pipeline:
    return Pipeline([

        node(
            func=split_data_for_evaluation,
            inputs="pre_data",
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_for_evaluation_node"
        )

    ])



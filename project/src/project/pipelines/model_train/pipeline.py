"""
This is a boilerplate pipeline 'model_train'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_model,
            inputs=["X_train", "y_train"],
            outputs = "model",
        )
    ])


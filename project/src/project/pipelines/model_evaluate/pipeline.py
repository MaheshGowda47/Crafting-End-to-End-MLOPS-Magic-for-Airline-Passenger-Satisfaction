"""
This is a boilerplate pipeline 'model_evaluate'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, node
from .nodes import evaluate_model

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=evaluate_model,
            inputs=["model", "X_test", "y_test"],
            outputs=None
        )
    ])


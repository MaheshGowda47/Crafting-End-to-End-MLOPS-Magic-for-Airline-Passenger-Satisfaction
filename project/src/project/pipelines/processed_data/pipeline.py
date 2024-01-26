"""
This is a boilerplate pipeline 'processed_data'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import preprocessed_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocessed_data,
            inputs="raw_data",
            outputs="pre_data",
        )
    ])



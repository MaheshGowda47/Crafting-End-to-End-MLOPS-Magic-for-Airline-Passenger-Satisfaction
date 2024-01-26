"""
This is a boilerplate pipeline 'data_split'
generated using Kedro 0.19.1
"""
import logging
import pandas as pd 
from sklearn.model_selection import train_test_split

def split_data_for_evaluation(pre_data: pd.DataFrame) -> pd.DataFrame:
    """
    Splits the data into training and testing sets for evaluation purposes.

    Args:
    - pre_data (pd.DataFrame): The input data.

    Returns:
    - X_train, X_test, y_train, y_test (pd.DataFrame): Split data for evaluation.
    """
    try:
        X = pre_data.drop(["Satisfaction"], axis=1)
        y = pre_data["Satisfaction"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error(f"Error occurred in split_data_for_evaluation: {e}")
        raise e




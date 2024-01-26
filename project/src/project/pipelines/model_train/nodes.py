"""
This is a boilerplate pipeline 'model_train'
generated using Kedro 0.19.1
"""
import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train) -> pd.DataFrame:
    """
    Trains a Random Forest Classifier on the provided training data.

    This function initializes a Random Forest Classifier with specified hyperparameters
    and fits the model on the given training data.

    Parameters:
    - X_train (DataFrame or array-like): Features for training.
    - y_train (Series or array-like): Target labels for training.

    Returns:
    - RandomForestClassifier: Trained Random Forest Classifier model.

    Raises:
    - Any Exception: Logs the error and raises the exception encountered during model training.
    """

    try:
        # Initialize the Random Forest Classifier with specific hyperparameters
        model = RandomForestClassifier()
        
        # Train the model on the provided training data
        model.fit(X_train, y_train)
        
        return model
    
    except Exception as e:
        # Log the error and raise the exception
        logging.error(f"Error occurred in train_model: {e}")
        raise e


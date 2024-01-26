"""
This is a boilerplate pipeline 'model_drift'
generated using Kedro 0.19.1
"""
import logging
import pandas as pd 
from .report import set_column_mapping
from .report import set_test_report
from .report import set_model_performance
from .report import set_classification_metrics
from sklearn.ensemble import RandomForestClassifier



def model_drift(pre_data: pd.DataFrame):
    try:
        # Slicing the data
        X_train = pd.DataFrame(pre_data.iloc[:64940, :12])
        X_test = pd.DataFrame(pre_data.iloc[64940:, :12])
        y_train = pd.Series(pre_data.iloc[:64940, -1])
        y_test = pd.Series(pre_data.iloc[64940:, -1])

        # Data preparation
        reference = pd.concat([X_train, y_train], axis=1)
        current = pd.concat([X_test, y_test], axis=1)

        # Model training
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Make predictions
        reference_pred = model.predict(X_train)
        current_pred = model.predict(X_test)

        # setting prediction column
        reference['prediction'] = reference_pred
        current['prediction'] = current_pred

        # setting column mapping
        column_mapping = set_column_mapping()

        # setting test report
        test_report = set_test_report(reference, current, column_mapping)
        test_report.save_html(r"data/06_model_drift/test_report.html")


        # setting model performance
        model_performance = set_model_performance(reference, current, column_mapping)
        model_performance.save_html(r"data/06_model_drift/model_performance.html")

        # setting class matrics
        class_metrics = set_classification_metrics(reference, current, column_mapping)
        class_metrics.save_html(r"data/06_model_drift/class_metics.html")

        return test_report, model_performance, class_metrics
    except Exception as e:
        logging.error(f"Error occurred in model_drift: {e}")
        raise e
    







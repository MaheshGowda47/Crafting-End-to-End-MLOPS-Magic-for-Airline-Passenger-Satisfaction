import pandas as pd
from typing import Any, Dict, Tuple
from evidently import ColumnMapping
from evidently.test_suite import TestSuite
from evidently.test_preset import DataQualityTestPreset, DataDriftTestPreset, DataStabilityTestPreset
from evidently.tests import *
from evidently.report import Report
from evidently.metrics import ClassificationClassSeparationPlot, ClassificationQualityByClass, ClassificationConfusionMatrix



"""column mapping"""
def set_column_mapping() -> Any:
    # Column Mapping
    target = "Satisfaction"
    prediction = "prediction"
    numerical_features = ['Age']
    categorical_features = ['flight_service_1', 'flight_service_2', 'flight_service_3','Gender', 'Customer Type', 'Type of Travel',
                   'Class', 'Flight Distance', 'Departure Delay', 'Arrival Delay', 'Departure and Arrival Time Convenience']

    column_mapping = ColumnMapping(
        target=target,
        prediction=prediction,
        numerical_features=numerical_features,
        categorical_features=categorical_features
    )
    return column_mapping


"""test_report"""
def set_test_report(
        reference_data : pd.DataFrame,
        current_data : pd.DataFrame,
        column_mapping : ColumnMapping,
):
    test_report = TestSuite(tests=[
        DataStabilityTestPreset(),
        DataDriftTestPreset(),
        DataQualityTestPreset(),
    ])
    test_report.run(reference_data=reference_data, current_data=current_data, column_mapping=column_mapping)
    return test_report

"""model_performance"""
def set_model_performance(
        reference_data : pd.DataFrame,
        current_data: pd.DataFrame,
        column_mapping: ColumnMapping,
):
    model_performance = TestSuite(tests=[
        TestTargetPredictionCorrelation(),
        TestAccuracyScore(),
    ])
    model_performance.run(reference_data=reference_data, current_data=current_data, column_mapping=column_mapping)
    return model_performance

"""classification_metrics"""
def set_classification_metrics(
        reference_data: pd.DataFrame,
        current_data: pd.DataFrame,
        column_mapping: ColumnMapping,
)-> Report:
    class_report = Report(metrics=[
        # ClassificationClassSeparationPlot(),
        ClassificationQualityByClass(),
        ClassificationConfusionMatrix(),
    ])
    class_report.run(reference_data=reference_data, current_data=current_data, column_mapping=column_mapping)
    return class_report
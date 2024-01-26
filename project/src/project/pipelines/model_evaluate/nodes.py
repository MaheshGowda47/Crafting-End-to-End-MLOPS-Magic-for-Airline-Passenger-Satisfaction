"""
This is a boilerplate pipeline 'model_evaluate'
generated using Kedro 0.19.1
"""
import logging
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def evaluate_model(model, X_test, y_test) -> None:
    """
    Evaluates the provided model using test data and saves evaluation metrics to an HTML file.

    Args:
    - model: The trained model to be evaluated.
    - X_test: Test features.
    - y_test: Test labels.
    """
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        # print(f"Accuracy: {accuracy:.2f}")

        # print("\nClassification Report:")
        class_report = classification_report(y_test, y_pred, output_dict=True)
        # print(classification_report(y_test, y_pred))

        # print("\nConfusion Matrix:")
        conf_matrix = confusion_matrix(y_test, y_pred)
        # print(conf_matrix)

        # Create a DataFrame from the classification report and confusion matrix
        metrics_dict = {
            "Accuracy": accuracy,
            "Precision_0": class_report['0']['precision'],
            "Precision_1": class_report['1']['precision'],
            "Recall_0": class_report['0']['recall'],
            "Recall_1": class_report['1']['recall'],
            "F1-score_0": class_report['0']['f1-score'],
            "F1-score_1": class_report['1']['f1-score'],
            "Support_0": class_report['0']['support'],
            "Support_1": class_report['1']['support'],
            "TN": conf_matrix[0][0],
            "FP": conf_matrix[0][1],
            "FN": conf_matrix[1][0],
            "TP": conf_matrix[1][1]
        }

        metrics_df = pd.DataFrame([metrics_dict])

        # Convert DataFrame to HTML and save to a file
        metrics_html = metrics_df.to_html("Evaluate_report/metrics.html", index=False)

    except Exception as e:
        # Log and raise an error in case of an exception during evaluation
        logging.error(f"Error occurred in model_evaluation: {e}")
        raise e







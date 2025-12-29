"""
Training helpers for the logistic regression baseline.
"""

from typing import Any, Dict

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from blue_dollar_ml.models.datasets import load_feature_dataset, temporal_split
from blue_dollar_ml.models.preprocessing import scale_features


def train_logistic_regression(features_csv: str | None = None) -> Dict[str, Any]:
    """
    Train the logistic regression model using the engineered features dataset.
    """

    df, feature_columns = load_feature_dataset(features_csv)
    x = df[feature_columns]
    y = df["target_up"]

    # Keep the chronological order: train -> validation -> test.
    (x_train, y_train), (x_val, y_val), (x_test, y_test) = temporal_split(x, y)
    scaler, (x_train_scaled, x_val_scaled, x_test_scaled) = scale_features(x_train, x_val, x_test)

    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(x_train_scaled, y_train)

    test_predictions = model.predict(x_test_scaled)
    accuracy = accuracy_score(y_test, test_predictions)

    return {
        "model": model,
        "scaler": scaler,
        "accuracy": accuracy,
        "predictions": test_predictions,
        "y_test": y_test,
        "x_val_scaled": x_val_scaled,
        "y_val": y_val,
    }


def main() -> None:
    result = train_logistic_regression()
    print("\nResultados del Gran Desafío:")
    print(f"Modelo con Features Avanzados: {result['accuracy']:.2%}")
    print("Baseline a vencer (Como Ayer): 58.68%")
    if result["accuracy"] > 0.5868:
        print("¡OBJETIVO CUMPLIDO! Tu modelo aprendió patrones reales.")
    else:
        print("Seguimos empatados o perdiendo. Necesitamos modelos más complejos.")

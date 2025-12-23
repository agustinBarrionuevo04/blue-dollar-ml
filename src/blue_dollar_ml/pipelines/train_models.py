"""
High-level script to train the available models in one go.
"""

from __future__ import annotations

from blue_dollar_ml.models.logistic_regression import train_logistic_regression
from blue_dollar_ml.models.random_forest import train_random_forest


def run_training_suite() -> dict:
    """
    Train every model so notebooks can reuse the metrics without duplicating
    logic.
    """

    logistic_result = train_logistic_regression()
    rf_result = train_random_forest()
    return {"logistic_regression": logistic_result, "random_forest": rf_result}


def main() -> None:
    results = run_training_suite()
    for model_name, payload in results.items():
        print(f"{model_name.replace('_', ' ').title()}: {payload['accuracy']:.2%}")


if __name__ == "__main__":
    main()


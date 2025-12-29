"""
Shared preprocessing utilities for model features.
"""

from typing import Tuple

from sklearn.preprocessing import StandardScaler


def scale_features(x_train, x_val, x_test) -> Tuple[StandardScaler, tuple]:
    """
    Standardize the features using statistics from the training set only.
    """

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_val_scaled = scaler.transform(x_val)
    x_test_scaled = scaler.transform(x_test)
    return scaler, (x_train_scaled, x_val_scaled, x_test_scaled)


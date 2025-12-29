"""
Very simple baseline strategies used for sanity-check comparisons.
"""

import numpy as np
import pandas as pd


class BaselineModel:
    """Simple interface so that baseline predictors share a signature."""

    def predict(self, features: pd.DataFrame) -> np.ndarray:  # pragma: no cover - protocol like behaviour
        raise NotImplementedError


class AlwaysUp(BaselineModel):
    """Predict that the price will always go up."""

    def predict(self, features: pd.DataFrame) -> np.ndarray:
        return np.ones(len(features), dtype=int)


class SameAsYesterday(BaselineModel):
    """
    Predict the direction using the ``lag_1`` column (yesterday variation).
    """

    def predict(self, features: pd.DataFrame) -> np.ndarray:
        if "lag_1" not in features.columns:
            raise ValueError("Feature set must contain a 'lag_1' column for this baseline.")
        return (features["lag_1"] > 0).astype(int).to_numpy()


def relative_strength_index(values: pd.Series, periods: int = 14) -> pd.Series:
    """
    Compute the RSI indicator for convenience when exploring features.
    """

    delta = values.diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # EWM replicates the RSI's smoothing factor.
    avg_gain = gain.ewm(com=periods - 1, adjust=False).mean()
    avg_loss = loss.ewm(com=periods - 1, adjust=False).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

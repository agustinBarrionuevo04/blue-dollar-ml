"""
Reusable helpers to load tabular datasets used by the models.
"""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import pandas as pd

from blue_dollar_ml.config import PROCESSED_DATA_DIR


def load_feature_dataset(
    features_csv: str | Path | None = None,
) -> Tuple[pd.DataFrame, list[str]]:
    """
    Load the engineered feature dataset used by the ML models.
    """

    dataset_path = (
        Path(features_csv) if features_csv is not None else PROCESSED_DATA_DIR / "features_advanced.csv"
    )
    df = pd.read_csv(dataset_path, parse_dates=["fecha"], index_col="fecha")

    # The RSI is calculated with current-day data, therefore we shift it to
    # avoid leaking the answer into the model.
    rsi_columns = [column for column in df.columns if "rsi" in column.lower()]
    if rsi_columns:
        df[rsi_columns] = df[rsi_columns].shift(1)

    df.dropna(inplace=True)
    df["returns"] = df["valor"].pct_change()
    df["target_up"] = (df["returns"] > 0).astype(int)
    df.dropna(inplace=True)

    features = [column for column in df.columns if column not in {"returns", "target_up", "valor"}]
    return df, features


def temporal_split(
    features: pd.DataFrame,
    target: pd.Series,
    *,
    train_ratio: float = 0.70,
    val_ratio: float = 0.15,
):
    """
    Deterministically split a time-ordered dataset keeping the chronological
    order intact. The remainder goes into the test set.
    """

    total_rows = len(features)
    train_idx = int(total_rows * train_ratio)
    val_idx = int(total_rows * (train_ratio + val_ratio))

    # Using iloc because the index is time based but we only need positions.
    x_train = features.iloc[:train_idx]
    y_train = target.iloc[:train_idx]

    x_val = features.iloc[train_idx:val_idx]
    y_val = target.iloc[train_idx:val_idx]

    x_test = features.iloc[val_idx:]
    y_test = target.iloc[val_idx:]

    return (x_train, y_train), (x_val, y_val), (x_test, y_test)


__all__ = ["load_feature_dataset", "temporal_split"]


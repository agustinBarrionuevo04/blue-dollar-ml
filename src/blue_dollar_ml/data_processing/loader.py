"""
Loading utilities for the dollar blue dataset.
"""

from pathlib import Path

import pandas as pd

from blue_dollar_ml.config import PROCESSED_DATA_DIR


def load_blue_data(source_csv: str | Path, *, output_csv: str | Path | None = None) -> pd.DataFrame:
    """
    Read the raw dataset, coerce the ``fecha`` column to datetime, order it by
    date and optionally re-export the clean data.
    """

    source_path = Path(source_csv)
    df = pd.read_csv(source_path)
    df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d")
    df = df.sort_values(by="fecha")

    if output_csv is None:
        output_path = PROCESSED_DATA_DIR / "blue_data_clean.csv"
    else:
        output_path = Path(output_csv)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return df


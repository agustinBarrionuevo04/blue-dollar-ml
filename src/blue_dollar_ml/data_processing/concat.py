"""
Helpers to combine processed CSV files.
"""

from pathlib import Path

import pandas as pd

from blue_dollar_ml.config import PROCESSED_DATA_DIR


def concat_csv_files(
    first_csv: str | Path, second_csv: str | Path, *, output_name: str = "combined"
) -> Path:
    """
    Concatenate two CSV files and write the result inside ``data/processed``.
    """

    first_df = pd.read_csv(first_csv)
    second_df = pd.read_csv(second_csv)
    combined = pd.concat([first_df, second_df], ignore_index=True)

    output_path = PROCESSED_DATA_DIR / f"{output_name}.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(output_path, index=False)
    return output_path


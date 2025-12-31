"""
Utilities to homogenize and clean the raw CSV files consumed by the project.

The functions intentionally accept explicit input/output paths so they can be
reused from notebooks, tests or pipelines without rewriting logic.
"""

from pathlib import Path
import pandas as pd
from blue_dollar_ml.config import PROCESSED_DATA_DIR


def format_category_dates(
    source_csv: str | Path,
    output_csv: str | Path | None = None,
    *,
    original_format: str = "%a %b %d %Y",
    target_format: str = "%Y-%m-%d",
) -> Path:
    """
    Read a CSV containing a `category` column with textual dates and convert
    those values into ISO formatted strings.
    """

    source_path = Path(source_csv)
    if output_csv is None:
        output_path = PROCESSED_DATA_DIR / f"{source_path.stem}_clean.csv"
    else:
        output_path = Path(output_csv)

    df = pd.read_csv(source_path)
    df["category"] = pd.to_datetime(df["category"], format=original_format)
    df["category"] = df["category"].dt.strftime(target_format)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path



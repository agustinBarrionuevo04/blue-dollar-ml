"""
Wrapper script that combines the available data processing utilities.
"""

from blue_dollar_ml.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
from blue_dollar_ml.data_processing.cleaning import format_category_dates
from blue_dollar_ml.data_processing.concat import concat_csv_files
from blue_dollar_ml.data_processing.loader import load_blue_data


def run_data_pipeline() -> None:
    """
    Clean the raw CSVs and concatenate the processed snapshots when posible.
    """

    load_blue_data(RAW_DATA_DIR / "dataDolar.csv")

    actual_csv = format_category_dates(
        RAW_DATA_DIR / "blue.csv",
        PROCESSED_DATA_DIR / "actually_data_filter.csv",
    )

    historical_csv = PROCESSED_DATA_DIR / "old_data_filter.csv"
    if historical_csv.exists():
        concat_csv_files(historical_csv, actual_csv, output_name="info_finally")


def main() -> None:
    run_data_pipeline()
    print("Pipeline de datos ejecutado correctamente.")


main()

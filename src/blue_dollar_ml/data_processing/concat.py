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


def concat_dollar_official_and_dollar_blue(first_csv: str | Path, second_csv: str | Path):
    try:
        if not Path(first_csv).is_file():
            raise FileNotFoundError(f"El archivo {first_csv} no existe.")
        if not Path(second_csv).is_file():
            raise FileNotFoundError(f"El archivo {second_csv} no existe.")

        df_dollar_official = pd.read_csv(first_csv, parse_dates=['fecha'], index_col='fecha')
        df_dollar_blue = pd.read_csv(second_csv, parse_dates=['fecha'], index_col='fecha')
        
        df_finally = pd.concat([df_dollar_blue, df_dollar_official], axis=1)
        df_finally.to_csv('/home/agusitn/Documents/projects/blue-dollar-ml/data/processed/dollar_official-dollar_blue.csv')
        return True
    except Exception as e:
        return f"Error al concatenar los CSV: {e}"
    
    
def main():
    try:    
        first_csv = '/home/agusitn/Documents/projects/blue-dollar-ml/data/processed/official-dollar.csv'
        second_csv = '/home/agusitn/Documents/projects/blue-dollar-ml/data/processed/info_finally.csv'
        is_succes = concat_dollar_official_and_dollar_blue(first_csv, second_csv)
        
        return "Proceso finalizado correctamente."
    except Exception as e:
        return f"Error en el proceso principal: {e}"


if __name__ == "__main__":
    main()
    print(main())
     
    


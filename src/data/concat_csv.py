import pandas as pd


def concat_csv(file_path_a, file_path_b, name_finally_csv):
    
    file_name = str(name_finally_csv)

    df_a = pd.read_csv(file_path_a)
    df_b = pd.read_csv(file_path_b)

    df_finally = pd.concat([df_a, df_b], ignore_index=True)
    df_finally.to_csv(f'/home/agusitn/Documents/projects/blue-dollar-ml/data/processed/{file_name}.csv', index=False)


fp_a = '/home/agusitn/Documents/projects/blue-dollar-ml/data/processed/old_data_filter.csv'
fp_b = '/home/agusitn/Documents/projects/blue-dollar-ml/data/processed/actually_data_filter.csv'

concat_csv(fp_a, fp_b, 'info_finally')

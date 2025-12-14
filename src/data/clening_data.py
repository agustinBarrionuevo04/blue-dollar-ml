import pandas as pd


"""This method change the format in the dates in the files"""

def clening_data(file_path):
    df = pd.read_csv(file_path)
    df['category'] = pd.to_datetime(df['category'], format='%a %b %d %Y')

    finally_fomat = '%Y-%m-%d'
    df['category'] = df['category'].dt.strftime(finally_fomat)

    df.to_csv('/home/agusitn/Documents/projects/blue-dollar-ml/data/processed/actually_data_filter.csv', index=False)



clening_data('/home/agusitn/Documents/projects/blue-dollar-ml/data/raw/blue.csv')

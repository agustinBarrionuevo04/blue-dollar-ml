"""This module provides fuctions to load and preprocess the BLUE dataset."""

import pandas as pd


""" 
    This method loads the dollar blue dataset from a CSV file and preprocesses it.
    Converts date strings to datetime objects and orders the data by date.
    Saves the processed date to a new CSV file in data/processed/blue_data_clean.csv.
"""

def load_blue_data(file_path):
    data = pd.read_csv(file_path)
    data['fecha'] = pd.to_datetime(data['fecha'], format='%Y-%m-%d')
    data = data.sort_values(by='fecha')
    data.to_csv("/home/agusitn/Documents/projects/blue-dollar-ml/data/processed/blue_data_clean.csv", index=False)
    return data 


load_blue_data("/home/agusitn/Documents/projects/blue-dollar-ml/data/raw/dataDolar.csv")
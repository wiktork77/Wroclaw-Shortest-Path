import os
import numpy as np
import pandas as pd
from IPython.display import display


def get_data_source_path(file_name):
    current_dir = os.getcwd()
    paths_dir = os.path.join(current_dir, "data_sources")
    data_file = os.path.join(paths_dir, file_name)
    return data_file


def retrieve_data(file_name):
    data_file = get_data_source_path(file_name)
    df = pd.read_csv(data_file, low_memory=False, usecols=[i + 1 for i in range(10)])
    return df


def display_data(df):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    display(df)


def get_raw_row(series):
    raw_row = ""
    for key in series.keys():
        raw_row += f"{str(series[key])},"
    return raw_row[:-1]



import pandas as pd

from .constants import DATA_FILE_PATH


def get_data_file(file_name=DATA_FILE_PATH):
    return pd.read_excel(file_name)

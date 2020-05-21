import pandas as pd

from .constants import DATA_FILE_PATH


def get_data_file(file_name=DATA_FILE_PATH):
    """
    Reads the data from the provided excel file
    :param file_name: an excel file
    :return: data in the excel file
    """
    return pd.read_excel(file_name)

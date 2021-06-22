"""
Author: Amanjot Singh
Student number: 040956152

This class is responsible for reading and writing data to files.
"""

import pandas as pd


def import_data():
    """
    This method uses the pandas library to read the file. read_csv accepts various arguments, first of which is file
    name, then the index of columns to be imported and then the number of rows to be imported. The method uses error
    handing to deal with missing files.
    :return: returns the loaded data as a DataFrame object or error message if file not found
    """

    try:
        data = pd.read_csv("data/covid19.csv",
                           usecols=['pruid', 'prname', 'prnameFR', 'date',
                                    'numconf', 'numprob', 'numdeaths',
                                    'numtotal', 'numtoday', 'ratetotal'])
        df = data.fillna(0)
        return df

    except FileNotFoundError:
        print("File not found, try again")


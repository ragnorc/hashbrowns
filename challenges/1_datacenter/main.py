# Google Hash Code: Data Center
import numpy as np
import pandas as pd


def physical_matrix(info_line, unavailable):
    """ Create numpy matrix with 0s and unavailable slots with 1st and 2nd line as args"""

    # Numpy 0 matrix for rows + cols ; "x" = unavailable
    server_matrix = np.zeros((info_line.iloc[0], info_line.iloc[1]))


def data_parser():
    """ Parses the data file and calls function depending on the input line """

    # Read data in pandas df and apply "SLots" and "Rows" as headers:
    input_data = pd.read_csv('dc.in', delim_whitespace=True, header=None)  # Line 0 = "x"

    # Extract line with info + int conversion:
    info_line = input_data.iloc[0].astype(int)
    unavailable = input_data.iloc[1].dropna(how='all').astype(int)  # still had NaN

    # Remove info_line + unavailable from df:
    input_data.drop([input_data.index[0], input_data.index[1]], inplace=True)

    # Reshape data by removing NaN:
    input_data.dropna(axis=1, how='all', inplace=True)

    # Reset index:
    input_data.reset_index(drop=True, inplace=True)

    # Add headers:
    input_data.columns = ['Slots', 'Rows']

    # Convert to integer:
    input_data = input_data.astype(int)

    # Create numpy matrix:
    physical_matrix(info_line, unavailable)


if __name__ == "__main__":
    data_parser()

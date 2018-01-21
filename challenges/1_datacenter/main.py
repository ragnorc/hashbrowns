# Google Hash Code: Data Center
import numpy as np
import pandas as pd


def matrix_maker(info_line, unavailable):
    """ Create numpy matrix with 0s and unavailable slots with 1st and 2nd line as args"""

    # Numpy 0 matrix for rows + cols ; 1 = unavailable
    server_matrix = np.zeros((info_line.iloc[0], info_line.iloc[1]))  # Shape = (16, 100)

    # For loop for all unavailable:
    for i in range(0, info_line.iloc[2]):

        # Change unavailable to 1:
        server_matrix[unavailable.iloc[i][0]][unavailable.iloc[i][1]] = 1

    print(server_matrix)


def data_parser():
    """ Parses the data file and calls function depending on the input line """

    # Read data in pandas df and apply "Slots" and "Rows" as headers:
    input_data = pd.read_csv('dc.in', delim_whitespace=True, header=None)  # Line 0 = "x"

    # Extract line with info + int conversion:
    info_line = input_data.iloc[0].astype(int)
    # unavailable = input_data.iloc[info_line[1::info_line[2]]].dropna(how='all').astype(int)  # still had NaN

    # Remove info_line from df:
    input_data.drop([input_data.index[0]], inplace=True)

    # Reshape data by removing NaN:
    input_data.dropna(axis=1, how='all', inplace=True)

    # Convert to integer:
    input_data = input_data.astype(int)

    # Reset index:
    input_data.reset_index(drop=True, inplace=True)

    # Add headers:
    input_data.columns = ['Rows', 'Slots']

    # Select unavailable (no need for -1 as df is re-indexed)
    unavailable = input_data.iloc[0:info_line[2]]  # RangeIndex: 80 entries, 0 to 79

    # Redefine input_data with servers to be placed:
    input_data = input_data.iloc[info_line[2]:]

    # Create numpy matrix:
    matrix_maker(info_line, unavailable)


if __name__ == "__main__":
    data_parser()

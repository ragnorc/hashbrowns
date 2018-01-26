# Google Hash Code: Data Center
import numpy as np
import pandas as pd

def space_trix(server_matrix):
    """ Calculate space available in each row in a 2D Array"""

    row_space_available = []  # 2D array
    for i in range(0, server_matrix.shape[0]):
        space = []  # array of uninterrupted spaces
        count = 0

        # iterate through rows and add 1:
        for x in np.nditer(server_matrix[i]):
            if x == 1:
                count += 1
            else:
                # If 0, append count:
                space.append(count)
                count = 0

        # Add spaces available in row to general array:
        row_space_available.append(space)

        # Cleans up memory
        del space

    print(row_space_available)
    print(server_matrix[2])


def matrix_maker(info_line, unavailable):
    """ Create numpy matrix with 0s and unavailable slots with 1st and 2nd line as args"""

    # Numpy 0 matrix for rows + cols ; 1 = unavailable
    server_matrix = np.ones((info_line.iloc[0], info_line.iloc[1]))  # Shape = (16, 100)

    # For loop for all unavailable:
    for i in range(0, info_line.iloc[2]):

        # Change unavailable to 1:
        server_matrix[unavailable.iloc[i][0]][unavailable.iloc[i][1]] = 0

    return server_matrix


def data_parser():
    """ Parses the data file and calls function depending on the input line """

    # Read data in pandas df and apply "Slots" and "Rows" as headers:
    input_data = pd.read_csv('dc.in', delim_whitespace=True, header=None)  # Line 0 = "x"

    # Extract line with info + int conversion:
    info_line = input_data.iloc[0].astype(int)

    # Remove info_line from df:
    input_data.drop([input_data.index[0]], inplace=True)

    # Reshape data by removing NaN:
    input_data.dropna(axis=1, how='all', inplace=True)

    # Convert to integer:
    input_data = input_data.astype(int)

    # Add headers:
    input_data.columns = ['Size', 'Capacity']

    # Select unavailable (no need for -1 as df is re-indexed)
    unavailable = input_data.iloc[0:info_line[2]]  # RangeIndex: 80 entries, 0 to 79

    # Redefine input_data with servers to be placed and reset index:
    input_data = input_data.iloc[info_line[2]:]
    input_data.reset_index(drop=True, inplace=True)

    # Create numpy matrix:
    dc_matrix = matrix_maker(info_line, unavailable)

    # Spacing in the matrix:
    space_trix(dc_matrix)

    print(input_data['Size'].value_counts())
    # 3
    # 135
    # 5
    # 126
    # 2
    # 126
    # 4
    # 125
    # 1
    # 113

if __name__ == "__main__":
    data_parser()

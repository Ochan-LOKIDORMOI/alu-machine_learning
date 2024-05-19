#!/usr/bin/env python3
""" implements the mat_mul function
"""


def mat_mul(mat1, mat2):
    """ multiplies two matrices together, every row, by every column
    """
    result = []

    # The number of rows and columns in the matrices
    n_rows_mat1 = len(mat1)
    n_rows_mat2 = len(mat2)
    n_cols_mat1 = len(mat1[0])
    n_cols_mat2 = len(mat2[0])

    # We can only multiply matrices if the number of columns in the
    # first matrix is equal.
    if n_cols_mat1 != n_rows_mat2:
        return None

    # From this point, we assume that the matrices can be multiplied
    for j in range(n_rows_mat1):
        row = []

        # The result matrix will have as many columns as the second matrix
        for k in range(n_cols_mat2):
            entry = 0

            # n represents the number of terms we are going to multiply
            n = n_cols_mat1

            for i in range(n):
                entry += mat1[j][i] * mat2[i][k]

            row.append(entry)

        result.append(row)

    return result

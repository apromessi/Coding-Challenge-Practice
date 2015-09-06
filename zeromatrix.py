def zero_matrix(matrix):
    """Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

    A matrix without zeroes doesn't change:

        >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    But if there's a zero, zero both that row and column:

        >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
        [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

    Make sure it works with non-square matrices:

        >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
    """

    for row_index, row in enumerate(matrix):
        for i, num in enumerate(row):
            if num == 0:
                for j in range(len(row)):
                    row[j] = 0
                for row in matrix:
                    row[i] = 0
                return matrix
    return matrix


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** TESTS PASSED! YOU'RE DOING GREAT!\n"

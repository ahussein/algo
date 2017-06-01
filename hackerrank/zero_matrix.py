"""
Zero matrix
"""

def zero_matrix(data):
    if len(data) == 0:
        return False
    rows = len(data)
    cols = len(data[0])
    rows_to_zero = set()
    cols_to_zero = set()
    for row_index in xrange(rows):
        for col_index in xrange(cols):
            if data[row_index][col_index] == 0:
                rows_to_zero.add(row_index)
                cols_to_zero.add(col_index)
    for row_index in rows_to_zero:
        for col_index in xrange(cols):
            data[row_index][col_index] = 0
    for col_index in cols_to_zero:
        for row_index in xrange(rows):
            data[row_index][col_index] = 0
    return True


def test():
    data = [[1, 2, 3], [4, 0, 6],[7, 8, 9]]
    zero_matrix(data)
    print(data)


if __name__ == '__main__':
    test()

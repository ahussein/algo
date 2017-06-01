"""
Rotate a matrix
"""

def rotate(data):
    if len(data) == 0 or len(data) != len(data[0]):
        return False

    size = len(data)
    for layer in xrange(size/2):
        first = layer
        last = size - 1 - layer
        for index in xrange(first, last):
            offset = index - first
            top = data[first][index]
            # left -> top
            data[first][index] = data[last-offset][first]
            # bottom -> left
            data[last-offset][first] = data[last][last-offset]
            # right -> bottom
            data[last][last-offset] = data[index][last]
            # top -> right
            data[index][last] = top
    return True

def test():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(data)
    print(data)


if __name__ == '__main__':
    test()

"""
Sum the content of array recursivly
"""

def sum_(data):
    """
    Sums the content of the array
    """
    size = len(data)
    if size == 0:
        return 0
    else:
        return sum_(data[:size-1]) + data[-1]


if __name__ == '__main__':
    data = [int(item) for item in input().split(' ')]
    print(sum_(data))

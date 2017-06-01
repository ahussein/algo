def reverse_(data, start, stop):
    """
    Reverse the elements in the array
    """
    if start >= stop:
        return
    else:
        tmp = data[start]
        data[start] = data[stop]
        data[stop] = tmp
        reverse_(data, start +1, stop -1)


if __name__ == "__main__":
    data = [int(item) for item in input().strip().split(' ')]
    reverse_(data, 0, len(data) - 1)
    print(data)

"""
Shuffle an arry
"""
import random

def shuffle(data):
    """
    Shuffles array data randomily
    """
    size = len(data)
    for index in range(size):
        r = random.randint(0, index+1)
        tmp = data[r]
        data[r] = data[index]
        data[index] = tmp


if __name__ == '__main__':
    data = input().split(' ')
    shuffle(data)
    print(data)

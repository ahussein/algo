#!/bin/python

"""
Solution for https://www.hackerrank.com/challenges/big-sorting
"""
import sys

def compare(a, b):
    result = 0
    if len(a) > len(b):
        result = 1
    elif len(a) < len(b):
        result = -1
    else:
        for index in xrange(len(a)):
            if a[index] > b[index]:
                result = 1
                break
            elif a[index] < b[index]:
                result = -1
                break
    return result

def sort(data):
    size = len(data)
    for index in xrange(1, size):
        inner_index = index - 1
        current = index
        while inner_index >= 0:
            if compare(data[current], data[inner_index]) == -1:
                data[current], data[inner_index] = data[inner_index], data[current]
                current = inner_index
            inner_index -= 1

def merge(left, right):
    left_size = len(left)
    right_size = len(right)
    result = [0] * (left_size + right_size)
    result_index = 0
    right_index = 0
    left_index = 0
    for index in xrange(left_size + right_size):
        if right_index == right_size:
            while left_index < left_size:
                result[result_index] = left[left_index]
                result_index += 1
                left_index += 1
            break
        if left_index == left_size:
            while right_index < right_size:
                result[result_index] = right[right_index]
                right_index += 1
                result_index += 1
            break
        if compare(left[left_index], right[right_index]) == -1:
            result[result_index] = left[left_index]
            result_index += 1
            left_index += 1
        else:
            result[result_index] = right[right_index]
            result_index += 1
            right_index += 1
    return result

def merge_sort(data):
    size = len(data)
    if size <= 1:
        return data
    mid = int(size/2)
    left = merge_sort(data[0:mid])
    right = merge_sort(data[mid:size])

    return merge(left, right)

n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)
# your code goes here
unsorted = merge_sort(unsorted)
for item in unsorted:
    print(item)

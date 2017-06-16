#!/bin/python

"""
Solution to problem https://www.hackerrank.com/challenges/reduced-string
"""
import sys

def reducable(s):
    index = 0
    inner_index = 1
    while inner_index < len(s):
        if s[index] == s[inner_index]:
            return True
        index += 1
        inner_index += 1
    return False

def super_reduced_string(s):
    # Complete this function
    if not reducable(s):
        return s
    index = 0
    inner_index = 1
    result = []
    while inner_index < len(s):
        if s[index] != s[inner_index]:
            result.append(s[index])
            index = inner_index
            inner_index = index + 1
        else:
            index = inner_index + 1
            inner_index = index + 1
    while index < len(s):
        result.append(s[index])
        index += 1
   
    return super_reduced_string(''.join(result)) if result else 'Empty String'

s = raw_input().strip()
result = super_reduced_string(s)
print(result)

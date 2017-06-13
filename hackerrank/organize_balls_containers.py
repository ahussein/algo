#!/bin/python

# algorithm to solve the problem mentioned here: https://www.hackerrank.com/challenges/organizing-containers-of-balls

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    M = []
    for M_i in xrange(n):
        M_temp = map(int,raw_input().strip().split(' '))
        M.append(M_temp)
    # your code goes here
    sv = []
    sh = []
    for index in xrange(n):
        sh.append(sum(M[index]))
        v_sum = 0
        for inner_index in xrange(n):
            v_sum += M[inner_index][index]
        sv.append(v_sum)
    sv.sort()
    sh.sort()
    if sv == sh:
        print('Possible')
    else:
        print('Impossible')

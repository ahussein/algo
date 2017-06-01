"""
To keep the description general
enough to be used with other puzzles, the algorithm enumerates and tests all k-
length sequences without repetitions of the elements of a given universe U . We
build the sequences of k elements by the following steps:
1. Recursively generating the sequences of k − 1 elements
2. Appending to each such sequence an element not already contained in it.
"""

def solve_puzzle(k, s, u):
    """
    solve puzzel for k length combination for a set 's'
    """
    for item in u:
        

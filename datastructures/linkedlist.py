"""
Linked list
"""

class Node:
    def __init__(self, data=None):
        self._data = data
        self._next = None
        self._prev = None

    def next(self):
        return self._next

    def has_next(self):
        return self._next is not None
    

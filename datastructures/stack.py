class IStack(object):
    def push(self, item):
        pass

    def pop(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass


class Stack(IStack):
    def __init__(self):
        self._size = -1
        self._data = []

    def push(self, item):
        self._size += 1
        self._data[self._size] = item

    def pop(self):
        if not self.is_empty():
            self._size -= 1
            return self._data[self._size + 1]


    def is_empty(self):
        return self._size == -1

    def size(self):
        return self._size

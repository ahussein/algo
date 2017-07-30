"""
If we have a map between digits 0-9 and characters so that each digit can represent a set of characters
given a number or array of integers 123 or [1, 2, 3], show all the possible string combination of this input sequence
Example:
given the map {0: 'ab', 1: 'cde', 2: 'fg'}
input: 201
output should be: [fac, fad, fae, fbc, fbd, fbe, gac, gad, gae, gbc, gbd, gbe]
"""

digit_map = {0: 'ab', 1: 'cde', 2: 'fg'}

def find_combinations(data):
    if len(data) == 1:
        return digit_map.get(data[0], '')
    sub_result = find_combinations(data[1:])
    current_digit = data[0]
    current_result = []
    for item in digit_map.get(current_digit, ''):
        for sub_item in sub_result:
            current_result.append('%s%s' % (item, sub_item))
    return current_result


def find_combinations_no_recurssion(data):
    if len(data) == 0:
        return
    class Stack:
        def __init__(self):
            self._size = 0
            self._data = list()

        def push(self, item):
            self._data.append(item)
            self._size += 1

        def pop(self):
            self._size -= 1
            return self._data.pop()

        def is_empty(self):
            return self._size == 0

        def print_(self):
            print(self._data, self._size)

    stack = Stack()
    for item in data:
        if item in digit_map:
            stack.push(digit_map[item])
    # stack.print_()
    # import pdb; pdb.set_trace()
    if not stack.is_empty():
        last_item = stack.pop()
        while not stack.is_empty():
            current_item = stack.pop()
            current_result = []
            for item in current_item:
                for sub_item in last_item:
                    current_result.append('%s%s' % (item, sub_item))
            if stack.is_empty():
                return current_result
            else:
                last_item = current_result



if __name__ == '__main__':
    data = [2, 0, 1]
    print(find_combinations(data))
    print(find_combinations_no_recurssion(data))

# nr_testcases = int(raw_input())
# data = []
# for _ in xrange(nr_testcases):
#     data.append(raw_input())

def reverse(data, start, end):
    while start < end:
        data[start], data[end-1] = data[end-1], data[start]
        start += 1
        end -= 1


def next_perm(data):
    """
    Find the next lexicographical permutation of a string
    algo:
    1) find the largest index k where a[k] < a[k+1], if not then stop, no more permutation avialable
    2) find the largest index l where a[k] < a[l]
    3) swap a[k] and a[l]
    4) reverse the rest of a starting from k+1 until the end
    """
    k = -1
    data = list(data)
    size = len(data)
    for index in xrange(size-1):
        if data[index] < data[index+1]:
            k = index
    if k == -1:
        return None
    l = k + 1
    for index in xrange(l, size):
        if data[k] < data[index]:
            l = index
    data[k], data[l] = data[l], data[k]
    reverse(data, k+1, size)
    return ''.join(data)


for item in data:
    result = next_perm(item)
    print(result or 'no answer')

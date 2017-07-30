"""
Implement pattern matching algorithms
"""

def boyer_moore_substring(text, pattern):
    """
    Exact match between pattern inside the given text

    Returns the least index in the text that starts the pattern
    """
    n, m = len(text), len(pattern)
    i, k = m -1, m -1
    if m == 0:
        return 0
    last_occurance = {}
    for index in xrange(m):
        last_occurance[pattern[index]] = index
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                k -= 1
                i -= 1
        else:
            j = last_occurance.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1



def test_boyer_moore_substring():
    print(boyer_moore_substring('abacaabadcabacabaabb', 'abacab'))



# kmp
def kmp_prefix(pattern):
    """
    Calculate a kmp prefix list for the given pattern
    """
    i , j  = 1, 0
    size = len(pattern)
    result = [0] * size
    while i < size:
        if pattern[i] == pattern[j]:
            result[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                result[i] = result[j]
                i += 1
            else:
                j = result[j-1]
    return result

def kmp_substr(text, pattern):
    """
    Implement a substring function using the KMP algorithm
    """
    output = []
    n, m = len(text), len(pattern)
    if n == 0 or m == 0:
        return output
    if m > n:
        return outupt
    i , jj = 0, 0
    prefix = kmp_prefix(pattern)
    while i < n:
        # if pattern is fully matched and the rest of the text is less than the pattern length then return the output
        if jj == m and n - i + 1 < m:
            output.append(i - m)
            return output
        elif jj == m:
            output.append(i - m)
            jj = 0
            i += 1
        if text[i] == pattern[jj]:
            i += 1
            jj += 1
        else:
            if m - prefix[jj] > n - i:
                return output
            if jj == 0:
                i += 1
            jj = prefix[max(jj-1, 0)]
    return output


def test_kmp_stubstr():
    print(kmp_substr('abacaabadcabacabaabb', 'abacab'))



"""
Longest common susequence algorithm
"""

def lcs(str1, str2):
    """
    Generates a table with longest common subsequences for each cell
    """
    # import pdb; pdb.set_trace()
    n, m = len(str1), len(str2)
    lcs_table = [[0] * (m +1) for k in xrange(n+1)]
    for index in xrange(1, n+1):
        for inner_index in xrange(1, m+1):
            if str1[index-1] == str2[inner_index-1]:
                lcs_table[index][inner_index] = 1 + lcs_table[index-1][inner_index-1]
            else:
                lcs_table[index][inner_index] = max(lcs_table[index][inner_index-1], lcs_table[index -1][inner_index])

    return lcs_table

def find_lcs(str1, str2):
    """
    Finds the longest common subsequence between two strings
    """
    lcs_table = lcs(str1, str2)
    n, m = len(str1), len(str2)
    index = n
    inner_index  = m
    result = []
    # import pdb; pdb.set_trace()
    while index > 0 or inner_index > 0:
        if lcs_table[index][inner_index] == lcs_table[index -1][inner_index]:
            index = index -1
        elif lcs_table[index][inner_index] == lcs_table[index][inner_index -1]:
            inner_index = inner_index -1
        else:
            result.append(str1[index-1])
            index -= 1
            inner_index -= 1
    return ','.join(reversed(result))

def print_lcs_table(str1, str2, table):
    print('    %s' % (' '.join(str1)))
    prefix = ' '
    for index, item in enumerate(table):
        if index != 0:
            prefix = str2[index-1]

        print('%s %s' % (prefix, ' '.join([str(item_) for item_ in item])))



if __name__ == '__main__':
    test_boyer_moore_substring()
    test_kmp_stubstr()
    print(kmp_prefix('aabaacaba'))
    print_lcs_table('abcdefg', 'akcdefl', lcs('abcdefg', 'akcdefl'))
    print(find_lcs('abcdefg', 'akcdefl'))

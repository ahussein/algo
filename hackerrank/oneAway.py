"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
-> true
pales. pale -> true
pale, pIe pale. bale -> true
pale. bake -> false
"""

def one_away(str1, str2):
    buffer = [0] * 256
    for index in xrange(len(str1)):
        buffer[ord(str1[index])] += 1
    for index in xrange(len(str2)):
        buffer[ord(str2[index])] -= 1
    nr_of_diffs = 0
    for index in xrange(len(buffer)):
        if buffer[index] != 0:
            nr_of_diffs += 1
            if nr_of_diffs > 2:
                return False
    if nr_of_diffs > 2:
        return False
    return True


def test():
    str1 = ['pales', 'pale', 'pale', 'pale']
    str2 = ['pale', 'ple', 'bale', 'bake']
    for index in xrange(len(str1)):
        print('%s, %s -> %s' % (str1[index], str2[index], one_away(str1[index], str2[index])))


if __name__ == '__main__':
    test()

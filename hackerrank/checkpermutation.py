def check_permutation(str1, str2):
    str1_length = len(str1)
    if str1_length != len(str2):
        return False
    str1_value, str2_value = 0, 0
    for index in range(str1_length):
        str1_value += ord(str1[index])
        str2_value += ord(str2[index])
    return str1_value == str2_value



if __name__ == '__main__':
    str1, str2 = input().split('||')
    print(check_permutation(str1, str2))

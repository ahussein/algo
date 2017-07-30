"""
Greg wants to build a string,  of length . Starting with an empty string, he can perform  operations:

Add a character to the end of  for  dollars.
Copy any substring of , and then add it to the end of  for  dollars.
Calculate minimum amount of money Greg needs to build .

Input Format

The first line contains number of testcases .

The  subsequent lines each describe a test case over  lines:
The first contains  space-separated integers, ,  , and , respectively.
The second contains  (the string Greg wishes to build).

Constraintsis composed of lowercase letters only.
Output Format

On a single line for each test case, print the minimum cost (as an integer) to build .

Sample Input

2
9 4 5
aabaacaba
9 8 9
bacbacacb
Sample Output

26
42
Explanation

Test Case 0:
 "";  ""
Append "";  ""; cost is
Append "";  ""; cost is
Append "";  ""; cost is
Copy and append "";  ""; cost is
Append "";  ""; cost is
Copy and append "";  ""; cost is

Summing each cost, we get , so our output for Test Case 1 is .

Test Case 1:
 "";  ""
Append "";  ""; cost is
Append "";  ""; cost is
Append "";  ""; cost is
Copy and append "";  ""; cost is
Copy and append "";  ""; cost is

Summing each cost, we get , so our output for Test Case 2 is .
"""


def build_longes_sbustring_table(data):
    size = len(data)
    table = [[0] * (size+1) for _ in xrange(size+1)]
    for index in xrange(1, size+1):
        for inner_index in xrange(1, size+1):
            if data[index-1] == data[inner_index-1]:
                table[index][inner_index] = table[index-1][inner_index-1] + 1
            else:
                table[index][inner_index] = 0
    return table


def find_longest_substring_optimized(index, substring_table):
    """
    find the longest substring using substring table
    """
    pass 



def find_longest_substring(source, data):
    if len(data) == 1:
      return data
    index = min(len(data), len(source))
    while index >= 0:
        if data[:index] and data[:index] in source:
            return data[:index]
        index -= 1
    return data[0]



def build_string(data, size, append_cost, copy_cost):
    if size == 0:
        return 0

    final_cost = append_cost
    target_str = [data[0]]
    index = 1
    min_cost = min(append_cost, copy_cost)
    # next_longest = ""
    while index < size:
        longest_substr = find_longest_substring(''.join(target_str), data[index:])
        # if index + 1 < size:
        #     next_longest = find_longest_substring(''.join(target_str + [data[index]]), data[index+1:])
        # longest_substr_size = max(len(longest_substr), len(next_long(est))
        # if len(next_longest) > len(longest_substr):
        #     longest_substr = next_longest
        #     final_cost += min_cost
        #     target_str.append(data[index])
        #     index += 1
        longest_substr_size = len(longest_substr)
        if append_cost * longest_substr_size < copy_cost:
            final_cost += append_cost * longest_substr_size
        else:
            final_cost += copy_cost
        target_str += list(longest_substr)
        index += longest_substr_size


    return final_cost

def test_build_string():
    print(build_string('aabaacaba', 9, 4, 5))
    print(build_string('bacbacacb', 9, 8, 9))


if __name__ == "__main__":
    # test_build_string()
    to_print = ' aabaacaba'
    substr_table = build_longes_sbustring_table('aabaacaba')
    print('  %s' % ' '.join(to_print))
    for row in xrange(len(substr_table)):
        print('%s %s' % (to_print[row], ' '.join([str(item_) for item_ in substr_table[row]])))

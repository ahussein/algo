class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        merger = list()
        a_index = 0
        b_index = 0
        result = 0.0
        for index in range(length):
            if a_index >= len(A):
                merger.extend(list(B)[b_index:])
                break
            elif b_index >= len(B):
                merger.extend(list(A)[a_index:])
                break
            else:
                if A[a_index] < B[b_index]:
                    merger.append(A[a_index])
                    a_index += 1
                else:
                    merger.append(B[b_index])
                    b_index += 1
        merger_length = len(merger)
        print merger
        if merger_length % 2 == 0:
            result = (merger[merger_length /2] + merger[merger_length/ 2 + 1]) / 2.0
        else:
            result = merger[merger_length]
        return result



if __name__ == '__main__':
    s = Solution()
    A = [ -50, -41, -40, -19, 5, 21, 28 ]
    B = [ -50, -21, -10 ]
    print s.findMedianSortedArrays(A, B)

'''
Given an array A of non-negative integers, return an array consisting of
all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
'''


class Solution:
    def sortArrayByParity(self, A):
        if not A:
            return []

        # Method 1
        # result = [item for item in A if (item % 2) == 0] + [item for item in A if (item % 2) == 1]
        # return result

        # Method 2
        # Quick sort approach

        left, right = 0, len(A) - 1
        while(left < right):
            if A[left] % 2 == 1 and A[right] % 2 == 0:
                A[left], A[right] = A[right], A[left]

            if A[left] % 2 == 0:
                left += 1
            if A[right] % 2 == 1:
                right -= 1
        return A

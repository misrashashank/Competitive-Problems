'''
Given two integer arrays A and B,
return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3

Explanation: 
The repeated subarray with maximum length is [3, 2, 1].

Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''


class Solution:
    def findLength(self, A, B):
        len_A, len_B = len(A), len(B)
        if len_A == 0 or len_B == 0:
            return 0

        # Initialize the DP matrix
        DP = [[0 for _ in range(len_A+1)] for _ in range(len_B+1)]

        # Update the DP matrix
        for row in range(1, len(DP)):
            for col in range(1, len(DP[0])):
                if A[col-1] == B[row-1]:
                    DP[row][col] = DP[row-1][col-1] + 1

        # Finding the maximum length of the subarray from the DP matrix
        max_len = 0
        for row in range(1, len(DP)):
            for col in range(1, len(DP[0])):
                if DP[row][col] > max_len:
                    max_len = DP[row][col]
        return max_len

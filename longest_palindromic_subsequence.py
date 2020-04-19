'''
Given a string s, find the longest palindromic subsequence's length in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
'''


class Solution:
    def longestPalindromeSubseq(self, s):
        len_s = len(s)
        if len_s == 0:
            return 0
        if len_s == 1:
            return 1

        DP = [[0 for _ in range(len_s+1)] for _ in range(len_s+1)]

        s_list = list(s)
        s_list_rev = list(s)[::-1]

        for row in range(1, len(DP)):
            for col in range(1, len(DP[0])):
                if s_list[row-1] == s_list_rev[col-1]:
                    DP[row][col] = DP[row-1][col-1] + 1
                else:
                    DP[row][col] = max(DP[row-1][col], DP[row][col-1])
        else:
            return DP[-1][-1]

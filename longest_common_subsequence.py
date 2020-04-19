'''
Given two strings text1 and text2, return the length of their
longest common subsequence.

A subsequence of a string is a new string generated from the original string
with some characters(can be none) deleted without changing the relative order
of the remaining characters.
(eg, "ace" is a subsequence of "abcde" while "aec" is not).
A common subsequence of two strings is a subsequence that is common
to both strings.

If there is no common subsequence, return 0.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
'''


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        len_1, len_2 = len(text1), len(text2)
        if len_1 == 0 or len_2 == 0:
            return 0

        DP = [[0 for _ in range(len_1+1)] for _ in range(len_2+1)]

        text1_list, text2_list = list(text1), list(text2)
        for row in range(1, len(DP)):
            for col in range(1, len(DP[0])):
                if text1_list[col-1] == text2_list[row-1]:
                    DP[row][col] = DP[row-1][col-1] + 1
                else:
                    DP[row][col] = max(DP[row-1][col], DP[row][col-1])

        return DP[-1][-1]

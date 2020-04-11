'''
Write a function to find the longest common prefix string
amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''


class Solution:
    def longestCommonPrefix(self, strs):
        # Maintain a string with matching characters from the start of the list
        # and pass it down the list
        # The matching characters string reduces in size as it encounters
        # new string in the list with uncommon characters

        if not strs:
            return ""

        self.common = strs[0]
        len_strs = len(strs)
        for index in range(1, len_strs):
            if len(strs[index]) == 0:
                return ""
            self.common = self.common_chars(strs[index])
            if len(self.common) == 0:
                return ""
        return self.common

    def common_chars(self, item):
        min_len = min(len(item), len(self.common))
        index = 0
        for index in range(min_len):
            if item[index] != self.common[index]:
                return self.common[:index]
        return self.common[:index+1]

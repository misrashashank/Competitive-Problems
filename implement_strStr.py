'''
Implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string?
This is a great question to ask during an interview.
'''


class Solution:
    def strStr(self, haystack, needle):
        len_haystack, len_needle = len(haystack), len(needle)

        if len_needle == 0:
            return 0

        for index in range(len_haystack - len_needle + 1):
            if haystack[index: index + len_needle] == needle:
                return index
        return -1

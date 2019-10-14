"""
Implement function ToLowerCase() that has a string parameter str,
and returns the same string in lowercase.

Example:
Input: "Hello"
Output: "hello"

Input: "here"
Output: "here"

Input: "LOVELY"
Output: "lovely"
"""


class Solution:
    def to_lower_case(self, str):
        """
        :type str: str
        :rtype: str
        """
        l_name = list(str)
        for ch in l_name:
            if ch.isupper():
                l_name[l_name.index(ch)] = chr(ord(ch)+32)
        return "".join(l_name)

        # OR
        # return str.lower()
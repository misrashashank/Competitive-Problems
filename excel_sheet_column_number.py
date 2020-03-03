'''
Given a column title as appear in an Excel sheet,
return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
'''


class Solution:
    def titleToNumber(self, s):
        s_list = list(s)
        s_value = [(ord(item) - 64) for item in s_list]
        s_value.reverse()

        len_nums = len(s_value)
        result = 0
        for index in range(len_nums):
            result += s_value[index] * (26 ** index)
        return result

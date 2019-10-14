"""
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number,
including the bounds if possible.

Example:
Input: left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
The boundaries of each input argument are 1 <= left <= right <= 10000.
"""


class Solution(object):
    def self_dividing_numbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output = []
        for num in range(left, right + 1):
            flag = 0
            str_num = str(num)
            for digit in str_num:
                if int(digit) == 0 or num % int(digit) != 0:
                    flag = 1
                    break
            if flag == 0:
                output.append(num)
        return output




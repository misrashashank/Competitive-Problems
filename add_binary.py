'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        string, string > string
        "11", "1" > "100"
        "1", "" > "1"

        Add leading zeroes if length not equal
        Traverse from right to left, manipulate on each element
        '''
        # Base case
        len_a, len_b = len(a), len(b)
        if len_a == 0:
            return b
        if len_b == 0:
            return a

        # Padding leading zeroes in shorter string
        if len_a != len_b:
            if len_a > len_b:
                b = '0' * (len_a - len_b) + b
            else:
                a = '0' * (len_b - len_a) + a

        index = len(a) - 1
        carry = 0
        output = [0] * len(a)

        while(index > -1):
            if int(a[index]) + int(b[index]) + carry == 0:
                output[index] = '0'
                carry = 0
            elif int(a[index]) + int(b[index]) + carry == 1:
                output[index] = '1'
                carry = 0
            elif int(a[index]) + int(b[index]) + carry == 2:
                output[index] = '0'
                carry = 1
            else:
                output[index] = '1'
                carry = 1
            index -= 1

        if carry == 1:
            output = ['1'] + output

        return "".join(output)

'''
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Example 1
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or
convert the inputs to integer directly.
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        String, String > String
        '2', '3' > '6'

        Helped method > Convert input to integer > Multiply > Convert to integer

        Time: O(n)
        Space: O(n)
        '''

        if len(num1) == 0 or len(num2) == 0:
            return "00"

        int1 = self.str_to_int(num1)
        int2 = self.str_to_int(num2)
        product = int1 * int2
        return str(product)

    def str_to_int(self, num_str):
        list_num = list(num_str)[::-1]
        sum = 0
        for index in range(len(list_num)):
            sum += int(list_num[index]) * (10 ** index)
        return sum

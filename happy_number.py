'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with 
any positive integer, replace the number by the sum of 
the squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 0: return False
        visited = [n]
        while(True):
            sum = 0
            digits = str(n)
            for item in digits:
                sum += int(item) ** 2
            if sum == 1:
                return True
            else:
                if sum in visited:
                    return False
                else:
                    visited.append(sum)
                    n = sum

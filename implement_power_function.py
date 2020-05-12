'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
'''


class Solution:
    def myPow(self, x, n):
        '''
        Float, Integer > Float
        
        2.10000, 3 > 9.26100
        2.00000, -2 > 0.25000
        0.0000, 4 > 0.0000
        
        Iterate for n times (n = power value). Keep all values in float.
        Power is negative > Divide result by 1
        Time: O(n)
        Space: O(1)
        This is time heavy.
        
        Better
        x, 10 > x * x * x ...10 times
        x * x ...5 times
        Known as Fast power method
        
        Time: O(log n)
        Space: O(1)
        '''
        
        # Method 1: Naive - Time heavy O(n)
        '''
        if n == 0:
            return float(1)
        if x == 0 or x == float(0):
            return x
        
        result = float(1.0)
        for _ in range(abs(n)):
            # print(result)
            result *= x
        # print(result)
        if n < 0:
            return float(1.0/result)
        return result
        '''
        
        # Method 2: Fast Power - Time: O(log n)
        
        # Check if power is negative
        if n < 0:
            x = 1/x

        return self.fast_power(x, abs(n))
    
    def fast_power(self, ele, power):
        if power == 0:
            return 1.0
        
        # Recursive call with n/2
        part = self.fast_power(ele, power//2)
        
        # Check if power was even or odd
        # Even power, result = part * part
        # Odd power, result = part * part * x (Due to n/2, one x is left out)
        if power % 2 == 0:
            return part * part
        else:
            return part * part * ele

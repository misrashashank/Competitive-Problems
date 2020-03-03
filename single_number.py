'''
Given a non-empty array of integers, every element appears twice
except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


class Solution:
    def singleNumber(self, nums):
        # To perform in O(n) time and constant space complexity
        # Take XOR of all elements. Result will be the element with frequency 1

        result = 0
        for item in nums:
            result ^= item
        return result

        # Method 2
        # Time O(n), but space used for Hash table

        nums_hash = {}
        for item in nums:
            if item in nums_hash:
                del nums_hash[item]
            else:
                nums_hash[item] = 1
        return nums_hash[0]

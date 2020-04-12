'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
'''


class Solution:
    def missingNumber(self, nums):
        # Method 1: Calculate target sum and find the missing number
        # Time: O(n)
        # Space: O(1)

        if nums == [0]:
            return 1
        if not nums or len(nums) == 1:
            return 0

        max_num = max(nums)
        target_sum = (max_num * (max_num + 1)) / 2
        nums_sum = sum(nums)
        if target_sum > nums_sum:
            return int(target_sum - nums_sum)
        else:
            if 0 in nums:
                return max_num+1
            else:
                return 0

        '''
        # Method 2: Using Hash Map
        # Time: O(n)
        # Space: O(n)
        nums_map = {}
        for item in nums:
            nums_map[item] = 1

        len_nums = len(nums)
        for item in range(len_nums + 1):
            if item not in nums_map:
                return item
        '''

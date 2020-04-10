'''
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        prev_max, prev_min = nums[0], nums[0]
        result = nums[0]
        curr_max, curr_min = nums[0], nums[0]

        len_nums = len(nums)
        for index in range(1, len_nums):
            curr_max = max(prev_min * nums[index],
                           prev_max * nums[index],
                           nums[index])

            curr_min = min(prev_min * nums[index],
                           prev_max * nums[index],
                           nums[index])

            result = max(result, curr_max)

            prev_max = curr_max
            prev_min = curr_min
        return result

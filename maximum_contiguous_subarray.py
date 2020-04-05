'''
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.
'''


class Solution:
    def maxSubArray(self, nums):
        '''
        # Method 1 - Greedy approach
        # Iterate over list and find local maximum sum, then update the
        # global maximum sum
        len_nums = len(nums)
        if len_nums == 0:
            return 0

        local_max, global_max = nums[0], nums[0]
        for index in range(1, len_nums):
            local_max = max(nums[index], local_max + nums[index])
            global_max = max(local_max, global_max)

        return global_max
        '''

        # Method 2 - Dynamic Programming
        # Modify the array - Iterate and modify the array
        # if local_sum > nums[index]

        len_nums = len(nums)
        if len_nums == 0:
            return 0

        global_sum = nums[0]
        for index in range(1, len_nums):
            # Modify the element only if adding the elements will be
            # greater than the current element
            if nums[index - 1] > 0:
                nums[index] = nums[index] + nums[index - 1]
            global_sum = max(global_sum, nums[index])
        return global_sum

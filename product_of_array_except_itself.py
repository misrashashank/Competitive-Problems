'''
Given an array nums of n integers where n > 1, return an array output
such that output[i] is equal to the product of all the elements of nums
except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of
space complexity analysis.)
'''


class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return []
        len_nums = len(nums)

        # Maintain arrays to store left and right flank multiplications
        left, right = [1] * len_nums, [1] * len_nums
        output = []

        # Update left array
        for index in range(1, len_nums):
            left[index] = left[index-1] * nums[index-1]

        for index in reversed(range(len_nums-1)):
            right[index] = right[index+1] * nums[index+1]

        # Create output array
        for index in range(len_nums):
            output.append(left[index] * right[index])

        return output

'''
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

'''
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums == 0:
            return nums
        left = 0
        for right in range(len_nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
'''

# New approach
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Array > None (in-place)
        [0,1,0,3,12] convert to [1,3,12,0,0]
        [0,0] > [0,0]
        [1,0,1] > [1,0,0]
        [] > []
        
        1,3,12,0,0
        Iterate > Pop and index-1 > Append
        
        Time: O(n)
        Space: O(1)
        '''
        
        len_nums = len(nums)
        index = 0
        for _ in range(len_nums):
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                index -= 1
            index += 1

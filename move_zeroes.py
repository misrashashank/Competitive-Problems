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


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        total_indexes = len(nums)
        sort_flag = 0
        for index in range(total_indexes):
            if nums[index] == 0:
                for next_index in range(index+1, total_indexes):
                    if nums[next_index] != 0:
                        temp = nums[next_index]
                        nums[next_index] = 0
                        nums[index] = temp
                        break
                    if next_index == total_indexes - 1:
                        sort_flag = 1
                        break
            if sort_flag == 1:
                break
        '''
        zeroes, non_zeroes = [], []
        for item in nums:
            if item == 0:
                zeroes.append(item)
            else:
                non_zeroes.append(item)
        non_zeroes.extend(zeroes)
        len_nums = len(nums)
        for index in range(len_nums):
            nums[index] = non_zeroes[index]

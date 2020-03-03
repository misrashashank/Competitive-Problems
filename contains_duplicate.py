'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''


class Solution:
    def containsDuplicate(self, nums):
        '''
        # Method 1
        nums.sort()
        len_nums = len(nums)
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                return True
        return False

        '''

        '''
        # Method 2
        nums.sort()
        nums_hash = {}
        for item in nums:
            if item in nums_hash:
                return True
            else:
                nums_hash[item] = 1
        return False
        '''

        '''
        # Method 3
        nums_set = set()
        for item in nums:
            if item in nums_set:
                return True
            else:
                nums_set.add(item)
        return False
        '''

        # Method 4
        return len(nums) != len(set(nums))

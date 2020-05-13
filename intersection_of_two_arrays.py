'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.
'''


class Solution:
    def intersection(self, nums1, nums2):
        '''
        Array, Array > Array
        
        nums1 = [4,9,5], nums2 = [9,4,9,8,4] > [9,4]
        
        n^2 > get element from 1, iterate over 2
        n > dict of 1st, iterate on 2nd
        
        Time: O(n)
        Space: O(n)
        '''
        
        if not nums1 or not nums2:
            return []
        
        nums1_map, result = {}, []
        for item in set(nums1):
            nums1_map[item] = 1
        
        for item in set(nums2):
            if item in nums1_map:
                result.append(item)
        return result

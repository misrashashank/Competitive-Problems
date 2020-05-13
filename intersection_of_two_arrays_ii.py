'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
1. What if the given array is already sorted?
How would you optimize your algorithm?

2. What if nums1's size is small compared to nums2's size?
Which algorithm is better?

3. What if elements of nums2 are stored on disk,
and the memory is limited such that you cannot load all elements
into the memory at once?
'''


from collections import defaultdict


class Solution:
    def intersect(self, nums1, nums2):
        '''
        Array, Array > Array
        
        nums1 = [4,9,5], nums2 = [9,4,9,8,4] > [4,9]
        nums1_map
        
        Time: O(n), Space: O(n)
        '''
        
        # Method 1: When arrays are not sorted
        '''
        if not nums1 or not nums2:
            return []
        
        nums1_map = defaultdict(int)
        result = []

        for item in nums1:
            nums1_map[item] += 1
        
        for item in nums2:
            if item in nums1_map and nums1_map[item] > 0:
                result.append(item)
                nums1_map[item] -= 1
        
        return result
        '''
    
        # Method 2
        # Follow-up question
        '''
        1. What if the given array is already sorted?
        How would you optimize your algorithm?
        Do a linear scan on both arrays simultaneously.
        If elements match > Add to result
        If elements don't match > Increment index of the array
        which has current element smaller

        Time: O(n), Space: O(1)
        '''
        if not nums1 or not nums2:
            return []
        
        # We will not count this in time complexity as we are assuming that
        # input arrays will be sorted
        nums1, nums2 = sorted(nums1), sorted(nums2)
        index_1, index_2 = 0, 0
        result = []

        while(index_1 < len(nums1) and index_2 < len(nums2)):
            if nums1[index_1] == nums2[index_2]:
                result.append(nums1[index_1])
                index_1 += 1
                index_2 += 1
            elif nums1[index_1] < nums2[index_2]:
                index_1 += 1
            else:
                index_2 += 1
        return result
        
        # Follow-up question
        '''
        What if nums1's size is small compared to nums2's size?
        Which algorithm is better?
        > Method 1 is better
        '''

        # Follow-up question
        '''
        What if elements of nums2 are stored on disk, and the memory is limited
        such that you cannot load all elements into the memory at once?
        > Use Method1 to create map for nums1 if it fits in memory
        If both arrays don't fit in memory > Then divide both in subarrays and
        use either methods
        '''

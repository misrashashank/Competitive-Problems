'''
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space
(size that is greater or equal to m + n)
to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        list, int, list, int
        [1,2,3,0,0,0], 3, [2,3,5], 3

        Time: O(m+n)
        Space: O(1)
        '''

        p1, p2 = m-1, n-1
        add_pointer = len(nums1) - 1
        while(p1 > -1 and p2 > -1):
            if nums1[p1] >= nums2[p2]:
                nums1[add_pointer] = nums1[p1]
                p1 -= 1
            else:
                nums1[add_pointer] = nums2[p2]
                p2 -= 1
            add_pointer -= 1
        nums1[:p2+1] = nums2[:p2+1]

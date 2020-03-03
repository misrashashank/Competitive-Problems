'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times
as it shows in both arrays. The result can be in any order.
'''


class Solution:
    def intersect(self, nums1, nums2):
        hash_nums1, hash_nums2, result = {}, {}, []

        for item in nums1:
            if item in hash_nums1:
                hash_nums1[item] += 1
            else:
                hash_nums1[item] = 1

        for item in nums2:
            if item in hash_nums2:
                hash_nums2[item] += 1
            else:
                hash_nums2[item] = 1

        for key in hash_nums1:
            if key in hash_nums2:
                count = min(hash_nums1[key], hash_nums2[key])
                result.extend([key] * count)

        return result

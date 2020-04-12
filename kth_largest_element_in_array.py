'''
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


from collections import defaultdict


class Solution:
    def findKthLargest(self, nums, k):
        if k == 0:
            return -1
        if k == 1:
            return max(nums)
        nums_map = defaultdict(int)
        for item in nums:
            nums_map[item] += 1

        nums_map = {k: v for k, v in sorted(nums_map.items(), key=lambda item: item[0], reverse=True)}
        for key, value in nums_map.items():
            k -= value
            if k < 1:
                return key

'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
'''


from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        if not nums:
            return None

        nums_map = defaultdict(int)
        for num in nums:
            nums_map[num] += 1

        nums_map = {k: v for k, v in sorted(nums_map.items(),
                                            key=lambda item: item[1],
                                            reverse=True)}

        all_elements = list(nums_map.keys())
        return all_elements[:k]

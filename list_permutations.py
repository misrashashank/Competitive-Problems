"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

import itertools

class Solution:
    def permute(self, nums):
        per = list(itertools.permutations(nums))
        for index in range(len(per)):
            per[index] = list(per[index])
        # per = map(list, per)
        return per
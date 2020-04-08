'''
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''


import collections


class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []

        # Initialize hash map to store grouped anagrams
        group_map = collections.defaultdict(list)

        for item in strs:
            group_map[tuple(sorted(item))].append(item)
        return group_map.values()

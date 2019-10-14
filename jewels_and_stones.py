"""
You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.  Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Input: J = "z", S = "ZZ"
Output: 0

Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""

import collections


class Solution:
    def num_jewels_in_stones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        # dict_S = collections.Counter(S)
        dict_S = {}
        for i in S:
            if i in dict_S.keys():
                dict_S[i] += 1
            else:
                dict_S[i] = 1

        for item in J:
            if item in dict_S.keys():
                count += dict_S[item]
        return count

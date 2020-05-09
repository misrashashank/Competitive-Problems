'''
Given two strings s1 and s2, write a function to return true
if s2 contains the permutation of s1.

In other words, one of the first string's permutations
is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''


from collections import defaultdict


class Solution:
    def checkInclusion(self, s1, s2):
        '''
        String, String > Boolean
        
        "ip", "hapiness" > True
        "ab", "eidbaooo" > True
        "cb", "eidbaooo" > False
        "cb", "" > False
        "", "eidbaooo" > False
        "", "" > False
        
        Create map for s1
        Slide window on s2 of size same as s1 > Map map from window > Check is maps match
        
        Time: O(n)
        Space: O(n)
        '''

        len_s1, len_s2 = len(s1), len(s2)
        if not s1 or not s2 or len_s1 > len_s2:
            return False
        
        # Create map for s1
        map_s1 = defaultdict(int)
        for item in s1:
            map_s1[item] += 1
        
        # Slide window over s2
        map_s2 = defaultdict(int)
        for index in range(len_s1):
            map_s2[s2[index]] += 1

        if map_s1 == map_s2:
            return True

        for index in range(len_s1, len_s2):
            # Remove index-1 element from map by 1 unit
            if map_s2[s2[index-len_s1]] == 1:
                del map_s2[s2[index-len_s1]]
            else:
                map_s2[s2[index-len_s1]] -= 1

            # Add index element in map_s2
            map_s2[s2[index]] += 1

            # Check if new mapping matches
            if map_s1 == map_s2:
                return True
        
        return False

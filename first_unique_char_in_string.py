'''
Given a string, find the first non-repeating character in it and
return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
'''


class Solution:
    def firstUniqChar(self, s):
        s_hash = {}
        for item in s:
            if item in s_hash:
                s_hash[item] += 1
            else:
                s_hash[item] = 1
        for item in s:
            if item in s_hash and s_hash[item] == 1:
                return s.index(item)
        return -1

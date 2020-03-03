'''
Given two strings s and t , write a function to determine if t
is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you
adapt your solution to such case?
'''


class Solution:
    def isAnagram(self, s, t):
        '''
        # Time: O(n^2)
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True

        t_list = list(t)
        for item in s:
            if item in t_list:
                t_list.remove(item)
            else:
                return False
        return True
        '''

        '''
        # Time: O(n log n)
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True

        s_sort = list(s)
        s_sort.sort()
        t_sort = list(t)
        t_sort.sort()
        s2 = "".join(s_sort)
        t2 = "".join(t_sort)
        if s2 == t2:
            return True
        else:
            return False
        '''

        # Time: O(n)
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        str_len = len(s)
        hash = {}

        for index in range(str_len):
            if s[index] in hash:
                hash[s[index]] += 1
            else:
                hash[s[index]] = 1

            if t[index] in hash:
                hash[t[index]] -= 1
            else:
                hash[t[index]] = -1
        print(hash)
        for value in hash.values():
            if value != 0:
                return False
        return True

'''
Given a string, find the length of the longest substring
without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        list_s = list(s)
        len_s = len(list_s)

        if s == "":
            return 0
        if s == " ":
            return 1

        # Maintain a hash map containing characters of a
        # non-repeating substring
        char_map = {}
        char_map[list_s[0]] = 0

        back, front = 0, 1
        max_count, count = 1, 1

        while(front < len_s):
            if list_s[front] not in char_map:
                char_map[list_s[front]] = front
                front += 1
                count += 1
                max_count = max(count, max_count)
            else:
                max_count = max(count, max_count)
                count = 1
                char_map = {}
                back += 1
                front = back + 1
                char_map[list_s[back]] = back
        return max_count

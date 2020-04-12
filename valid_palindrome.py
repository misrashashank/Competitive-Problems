'''
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem,
we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''


class Solution:
    def isPalindrome(self, s):
        if not s:
            return True

        ind_chars = [ele.lower() for ele in s if ele.isalnum()]
        s_original = "".join(ind_chars)
        s_reverse = s_original[::-1]
        return s_original == s_reverse

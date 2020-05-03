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
        '''
        str > Bool
        "race a car" > False
        "" > True
        
        Remove spaces and special chars, make lower > check reverse of string
        '''
        updated_str = [item.lower() for item in s if item.isalnum()]
        return updated_str == updated_str[::-1]

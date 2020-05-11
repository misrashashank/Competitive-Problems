'''
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''


class Solution:
    def letterCombinations(self, digits):
        '''
        String > Array
        
        "23" > ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        
        Recursion
        Create combination as:
            Take each digit
                For each digit, take each character mapped for each digit
                    When no digit left, combination formed > append        
        '''
        
        num_char_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []
    
        def create_combination(combination, next_digits):
            if not next_digits:
                result.append(combination)
            else:
                for character in num_char_map[next_digits[0]]:
                    create_combination(combination + character, next_digits[1:])

        if digits:
            create_combination("", digits)
        return result

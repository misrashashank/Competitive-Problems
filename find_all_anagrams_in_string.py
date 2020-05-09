'''
Given a string s and a non-empty string p,
find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and
the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output: [0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''


from collections import defaultdict


class Solution:
    def findAnagrams(self, s, p):
        '''
        String, String > Array
        
        "abab", "ab" > [0, 1, 2]
        "abab", "" > []
        "", "ab" > []
        "abab", "ababab" > [] Size of p greater than s

        Create map for p
        Slide p sized window on s, create mapping for window,
        check if this map matches map_p
        Slide window ahead > Remove left index mapping, add next index mapping
        '''
        
        if not s or not p or len(s) < len(p):
            return []
        
        # Create map for p
        map_p = defaultdict(int)
        for item in p:
            map_p[item] += 1

        # Slide a window on s of same size as p
        len_p = len(p)
        index, result = 0, []
        
        # Create window mapping
        map_window = defaultdict(int)
        window = s[index : index+len_p]
        for item in window:
            map_window[item] += 1
        if map_window == map_p:
            result.append(index)

        # Slide window over s
        while(index+len_p < len(s)):

            # Remove left-most element window mapping
            if map_window[s[index]] == 1:
                del map_window[s[index]]
            else:
                map_window[s[index]] -= 1
            
            # Add next element in window mapping
            map_window[s[index+len_p]] += 1

            if map_p == map_window:
                result.append(index+1)
            
            index += 1
        
        return result

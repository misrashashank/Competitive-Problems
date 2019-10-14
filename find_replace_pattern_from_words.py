"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x
in the pattern with p(x), we get the desired word.
(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.
You may return the answer in any order.

Example:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]

Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

Note:
1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20

"""

def find_numeric_pattern(string):
    set_string = sorted(set(string), key = string.index)
    dict_string, counter = {}, 0
    for item in set_string:
        dict_string[item] = counter
        counter += 1
    numeric_pattern = []
    for item in string:
        numeric_pattern.append(str(dict_string[item]))
    return "".join(numeric_pattern)
class Solution(object):
    def find_and_replace_pattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        output = []
        target = find_numeric_pattern(pattern)
        for item in words:
            new_word = find_numeric_pattern(item)
            if new_word == target:
                output.append(item)
        return output
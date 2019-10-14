"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and
uppercase letters only.
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
The rules of Goat Latin are as follows:
- If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

- If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

- Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin.

Example:
Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Notes:
S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.
"""


class Solution(object):
    def to_goat_latin(self, S):
        """
        :type S: str
        :rtype: str
        """
        list_S = S.split()
        output = []
        for index in range(len(list_S)):
            if ord(list_S[index][0]) in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]:
                list_string = list(list_S[index])
                list_string.append("ma" + "a"*(index+1))
                output.append("".join(list_string))
            else:
                list_string = list(list_S[index])
                list_string.append(list_string[0] + "ma" + "a"*(index+1))
                del list_string[0]
                output.append("".join(list_string))
        return " ".join(output)

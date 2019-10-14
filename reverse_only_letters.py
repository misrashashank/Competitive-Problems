"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
and all letters reverse their positions.

Example:
Input: "ab-cd"
Output: "dc-ba"

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:
S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""

"""
class Solution:
    def reverse_only_letters(self, S):
        """
        :type S: str
        :rtype: str
        """
        index, output, s_list, special = [], [], [], []
        for i in range(len(S)):
            if S[i].isalpha() == False:
                index.append(i)
                special.append(S[i])
            else:
                s_list.append(S[i])
        s_list = s_list[::-1]
        for i in range(len(S)):
            if i in index:
                output.append(special.pop(0))
            else:
                output.append(s_list.pop(0))
        return "".join(output)
"""

class Solution:
    def reverse_only_letters(self, S):
        """
        :type S: str
        :rtype: str
        """
        low, high, s = 0, len(S) - 1, list(S)
        while(low <= high):
            if s[low].isalpha() and s[high].isalpha():
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
            else:
                if not s[low].isalpha():
                    low += 1
                elif not s[high].isalpha():
                    high -= 1
        return "".join(s)

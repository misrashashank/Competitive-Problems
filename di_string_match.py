"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example:

Input: "IDID"
Output: [0, 4, 1, 3, 2]

Input: "III"
Output: [0, 1, 2, 3]

Input: "DDI"
Output: [3, 2, 0, 1]

Note:
1 <= S.length <= 10000
S only contains characters "I" or "D".
"""


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        """
        available = list(range(len(S)+1))
        result = []
        for item in S:
            if item == "I":
                a_min = min(available)
                result.append(a_min)
                del available[available.index(a_min)]
            else:
                a_max = max(available)
                result.append(a_max)
                del available[available.index(a_max)]
        result.append(available[0])
        return result
        """
        l, r, result = 0, len(S), []
        for item in S:
            if item == "I":
                result.append(l)
                l += 1
            else:
                result.append(r)
                r -= 1
        result.append(l)
        return result

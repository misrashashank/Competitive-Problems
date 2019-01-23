"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
Return the element repeated N times.

Example:

Input: [1,2,3,3]
Output: 3

Input: [2,1,2,5,3,2]
Output: 2

Input: [5,1,5,2,5,3,5,4]
Output: 5

Note:
4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""


import collections

class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dict_A = collections.Counter(A)
        # for key, item in dict_A.items():
        #     if item > 1:
        #         return key
        dict_A = {}
        for item in A:
            if item in dict_A.keys():
                return item
            else:
                dict_A[item] = 1

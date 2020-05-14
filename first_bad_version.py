'''
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out
the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return
whether version is bad. Implement a function to find the first bad version.
You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        Integer > Integer
        
        5 > [1,2,3,4,5] > 4 (First bad version)
        1 > [1] > 
        0 > None
        
        Array will be sorted as it's sequential
        Binary search 
                     b  b  b
        [1, 2, 3, 4, 5, 6, 7]
        '''
    
        if n == 0:
            return None
        if n == 1:
            return 1
        
        l, r = 0, n-1
        while(l <= r):
            mid = (l + r) // 2
            if isBadVersion(mid+1):
                r = mid - 1
                result = mid+1
            else:
                l = mid + 1
        return result

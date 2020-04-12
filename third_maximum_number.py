'''
Given a non-empty array of integers, return the third maximum number
in this array. If it does not exist, return the maximum number.
The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned.

Example 3:
Input: [2, 2, 3, 1]
Output: 1

Explanation: Note that the third maximum here means the third maximum
distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution:
    def thirdMax(self, nums):
        '''
        # Method 1: Using Set and deleting top 2 maximums
        # Time: O(n)
        # Space: O(n)

        if not nums:
            return -inf
        if len(nums) in [1, 2]:
            return max(nums)

        set_nums = set(nums)
        if len(set_nums) < 3:
            return max(set_nums)
        # Remove 2 maximums and return the next maximum
        max_num = max(set_nums)
        set_nums.remove(max_num)
        max_num = max(set_nums)
        set_nums.remove(max_num)
        return max(set_nums)
        '''

        # Method 2: Iterate array and maintain a set of 3 maximums
        # Return the smallest element in the set
        # Time: O(n)
        # Space: O(1)

        if not nums:
            return -inf
        if len(nums) in [1, 2]:
            return max(nums)

        max_3_set = set()
        for item in nums:
            max_3_set.add(item)
            if len(max_3_set) > 3:
                max_3_set.remove(min(max_3_set))
        if len(max_3_set) < 3:
            return max(max_3_set)
        return min(max_3_set)

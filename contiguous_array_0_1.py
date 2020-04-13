'''
Given a binary array, find the maximum length of a contiguous subarray
with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray
with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray
with equal number of 0 and 1.

Note:
The length of the given binary array will not exceed 50,000.
'''


class Solution:
    def findMaxLength(self, nums):
        # Maintain a count variable which is modified by the elements
        # '0' subtracts 1 and '1' adds 1 to the variable
        # Whenever count has a new unique value, add it to the hash map
        # When count has a value previously seen, that means sub-array found
        # Then, calculate the length from previously found count value
        # to current index

        # Time: O(n)
        # Space: O(n)

        if not nums:
            return 0

        count_map = {0: -1}
        count, max_length = 0, 0

        for index in range(len(nums)):
            new_length = 0
            if nums[index] == 0:
                count -= 1
            else:
                count += 1
            if count not in count_map:
                count_map[count] = index
            else:
                new_length = index - count_map[count]
            max_length = max(new_length, max_length)
        return max_length

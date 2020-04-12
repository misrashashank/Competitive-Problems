'''
Given an array, rotate the array to the right by k steps,
where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
Could you do it in-place with O(1) extra space?
'''


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        len_nums = len(self.nums)

        if len_nums < 2:
            return self.nums

        k = k % len_nums

        self.reverse_array(0, len_nums-1)
        self.reverse_array(0, k-1)
        self.reverse_array(k, len_nums-1)

    def reverse_array(self, start, end):
        while(start < end):
            self.nums[start], self.nums[end] = self.nums[end], self.nums[start]
            start += 1
            end -= 1

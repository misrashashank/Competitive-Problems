'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1],
find a peak element and return its index.

The array may contain multiple peaks,
in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return
the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1
where the peak element is 2, or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
'''

'''
# Solution 1
class Solution:
    def find_peak_element(self, nums):
        nums_len = len(nums)
        if nums_len > 2:
            mid = int(nums_len / 2)
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            else:
                left = nums[:mid]
                right = nums[mid + 1:]
                if len(left) > 2:
                    self.find_peak_element(left)
                if len(right) > 2:
                    self.find_peak_element(right)
        else:
            if nums_len == 2:
                if nums[0] > nums[1]:
                    return 0
                else:
                    return 1
            else:
                return nums[0]

sol_obj = Solution()
res = sol_obj.find_peak_element([1, 2, 1, 3])
print(res)
'''
'''
# Solution 2 - Recursion
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Array > Integer
        
        [1,2,1,3,5,6,4] > 1 (Index of the peak)
        
        log n > Binary search
        Find mid
            > If mid on downward slope > Go left
            > If mid on upward slope > Go right
            > No element left > Peak!
        '''
        
        if not nums:
            return None
        
        return self.binary_search(0, len(nums)-1, nums)
        
        
    def binary_search(self, l, r, nums):
        if l == r:
            return l
        
        mid = (l+r) // 2
        if nums[mid] < nums[mid + 1]:
            return self.binary_search(mid+1, r, nums)
        else:
            return self.binary_search(l, mid, nums)
'''        

# Solution 3 - Iterative
class Solution:
    def findPeakElement(self, nums):
        if not nums:
            return None

        len_nums = len(nums)
        l, r = 0, len_nums - 1
        while(l < r):
            mid = (l + r) // 2
            
            # Downward slope, one of the peaks is on the left
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid+1
        return l

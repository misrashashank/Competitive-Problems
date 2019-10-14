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
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for index, ele in enumerate(nums):
            if ele in diff:
                return [diff[ele], index]
            else:
                diff[target - ele] = index

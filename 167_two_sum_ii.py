class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        left, right = 0, size - 1
        for item in range(size):
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1


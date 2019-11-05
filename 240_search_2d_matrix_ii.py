# Time - O(m + n)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row, col, size = len(matrix) - 1, 0, len(matrix[0])
        while(row >= 0 and col < size):
            ele = matrix[row][col]
            if ele == target:
                return True
            elif ele > target:
                row -= 1
            else:
                col += 1
        return False
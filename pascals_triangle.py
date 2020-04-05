'''
Given a non-negative integer numRows,
generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers
directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        pascal_triangle = [[1], [1, 1]]
        upper_row = [1, 1]
        for row in range(2, numRows):
            new_row = [1]

            len_upper_row = len(upper_row)
            for index in range(1, len_upper_row):
                new_row.append(upper_row[index - 1] + upper_row[index])

            new_row.append(1)
            pascal_triangle.append(new_row)
            upper_row = new_row

        return pascal_triangle

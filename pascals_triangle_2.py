'''
Given a non-negative index k where k ≤ 33,
return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the
two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        curr_row = [1, 1]
        for row in range(2, rowIndex+1):
            new_row = [1]
            
            len_curr_row = len(curr_row)
            for index in range(1, len_curr_row):
                new_row.append(curr_row[index - 1] + curr_row[index])
            
            new_row.append(1)
            curr_row = new_row
        return curr_row
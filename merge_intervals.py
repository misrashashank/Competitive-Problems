'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]

Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


class Solution:
    def merge(self, intervals):
        '''
        Array > Array
        
        [[1,3],[2,6],[8,10],[15,18]] > [[1,6],[8,10],[15,18]]
        
        Sort intervals by 0th element
        [1, 4], [2, 6] > [1, 6]         Base
        [4, 12] [8, 10] > [4, 12]       Consume
        [2, 8], [1, 6] > [1, 8]
        
        i[1] >= i+1[0]      Can be merged
            min(0) and max(1)
            
        [1, 4], [2, 6], []
        
        Time: Sorting O(n log n), Iterate O(n) => O(n log n)
        Space: O(1)
        '''
        
        if not intervals:
            return []
        
        # Sort intervals by 0th or start index
        intervals.sort(key=lambda x: x[0])
        
        # Merge intervals
        merged_intervals = [intervals[0]]
        for index in range(1, len(intervals)):
            if merged_intervals[-1][1] >= intervals[index][0]:
                merged_intervals[-1] = [
                    min(merged_intervals[-1][0], intervals[index][0]),
                    max(merged_intervals[-1][1], intervals[index][1])
                ]
            else:
                merged_intervals.append(intervals[index])
        return merged_intervals

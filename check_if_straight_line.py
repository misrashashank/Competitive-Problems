'''
You are given an array coordinates, coordinates[i] = [x, y],
where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 
Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''


class Solution:
    def checkStraightLine(self, coordinates):
        '''
        Arrays > Boolean
        [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]] > False
        [] > True
        [[1,1]] > True
        
        Same slope > calculate slope
        Time: O(n)
        Space: O(1)
        '''

        len_coor = len(coordinates)
        if len_coor == 0 or len_coor == 1 or len_coor == 2:
            return True
        
        if (coordinates[1][0] - coordinates[0][0]) == 0:
            slope = 'inf'
        else:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for index in range(2, len_coor):
            print(index)
            if (coordinates[index][0] - coordinates[index-1][0]) == 0:
                new_slope = 'inf'
            else:
                new_slope = (coordinates[index][1] - coordinates[index-1][1]) / (coordinates[index][0] - coordinates[index-1][0])
            if new_slope != slope:
                return False
        return True

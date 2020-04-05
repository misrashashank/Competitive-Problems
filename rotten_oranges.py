'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally)
to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell
has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0)
is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0,
the answer is just 0.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''


class Solution:
    def orangesRotting(self, grid):
        grid_n_rows = len(grid)
        if grid_n_rows == 0:
            return -1
        grid_n_cols = len(grid[0])
        total_time = 0

        # Get indices of fresh and already rotten oranges
        fresh, already_rotten = [], []
        for row in range(grid_n_rows):
            for col in range(grid_n_cols):
                if grid[row][col] == 2:
                    already_rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh.append((row, col))

        # All the directions in which the oranges could get rotten
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # For every minute, convert fresh oranges to rotten
        while len(fresh) != 0:
            new_rotten = []
            for r, c in already_rotten:
                for direction_index in directions:
                    adj_x = r + direction_index[0]
                    adj_y = c + direction_index[1]

                    if -1 < adj_x < grid_n_rows and -1 < adj_y < grid_n_cols and grid[adj_x][adj_y] == 1:
                        grid[adj_x][adj_y] = 2
                        new_rotten.append((adj_x, adj_y))
                        fresh.remove((adj_x, adj_y))

            if len(new_rotten) == 0 and len(fresh) > 0:
                return -1

            # Newly rotten oranges
            already_rotten = new_rotten
            total_time += 1
        return total_time

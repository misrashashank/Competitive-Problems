'''
According to the Wikipedia's article: "The Game of Life, also known as
simply as Life, is a cellular automaton devised by the British mathematician
John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state
live (1) or dead (0). Each cell interacts with its eight neighbors
(horizontal, vertical, diagonal) using the following four rules
(taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies,
as if caused by under-population.
2. Any live cell with two or three live neighbors lives on
to the next generation.
3. Any live cell with more than three live neighbors dies,
as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell,
as if by reproduction.

Write a function to compute the next state (after one update) of the board
given its current state. The next state is created by applying the above rules
simultaneously to every cell in the current state,
where births and deaths occur simultaneously.

Example:
Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:
1. Could you solve it in-place? Remember that the board needs to be updated
at the same time: You cannot update some cells first and then use their
updated values to update other cells.

2. In this question, we represent the board using a 2D array.
In principle, the board is infinite, which would cause problems when
the active area encroaches the border of the array.
How would you address these problems?
'''


class Solution:
    '''
    # Method 1: O(mn) Space solution
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []

        # In order to do in-place, we will maintain
        # a copy of the board to reference

        self.num_rows, self.num_cols = len(board), len(board[0])
        self.board_ref = [[board[row][col] for col in range(self.num_cols)] for row in range(self.num_rows)]
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                ones_count = self.count_ones(row, col)
                if self.board_ref[row][col] == 1:
                    if ones_count < 2:
                        board[row][col] = 0
                    elif ones_count > 3:
                        board[row][col] = 0
                else:
                    if ones_count == 3:
                        board[row][col] = 1

    def count_ones(self, row, col):
        ones_count = 0
        for item in self.directions:
            neighbour_row = row + item[0]
            neighbour_col = col + item[1]
            if -1 < neighbour_row < self.num_rows and -1 < neighbour_col < self.num_cols and self.board_ref[neighbour_row][neighbour_col] == 1:
                ones_count += 1
        return ones_count
    '''

    # Method 2: Space O(1) solution
    def gameOfLife(self, board]):
        if not board:
            return []

        # In this approach, we don't maintain a copy of the board
        # We change the value to unique notations indicating the down steps
        # that there was a change in this value in upper steps
        # Notation: When a cell dies (1 -> 0), we change the value from 1 -> 3
        # Notation: When a cell comes to life (0 -> 1), we change the value from 0 -> 2
        # Basically, even values -> were originally dead and
        # odd values -> were originally alive
        # Essentially, we need to make changes in the count_ones() method
        # and after the whole board processing, we need to convert 2 -> 1 and 3 -> 0

        self.board = board
        self.num_rows, self.num_cols = len(self.board), len(self.board[0])
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                ones_count = self.count_ones(row, col)
                if self.board[row][col] == 1:
                    if ones_count < 2:
                        board[row][col] = 3
                    elif ones_count > 3:
                        board[row][col] = 3
                else:
                    if ones_count == 3:
                        board[row][col] = 2

        # Change the values 2 -> 1 and 3 -> 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.board[row][col] == 2:
                    self.board[row][col] = 1
                elif self.board[row][col] == 3:
                    self.board[row][col] = 0

    def count_ones(self, row, col):
        ones_count = 0
        for item in self.directions:
            neighbour_row = row + item[0]
            neighbour_col = col + item[1]
            if -1 < neighbour_row < self.num_rows and -1 < neighbour_col < self.num_cols:
                if self.board[neighbour_row][neighbour_col] % 2 == 1:
                    ones_count += 1
        return ones_count

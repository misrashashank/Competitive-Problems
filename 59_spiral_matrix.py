class spiral_matrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[-1 for i in range(n)] for j in range(n)]

    def print_matrix(self):
        for index in range(self.n):
            print(self.matrix[index])

    def generate_matrix(self):
        element, limit = 0, n**2 + 1
        row, col = 0, -1
        while(element < limit):
            while(col < n and self.matrix[row][col] == -1):
                col += 1
                self.matrix[row][col] = element
                element += 1
            self.print_matrix()
            print(row, col, element)

            while(row < n and self.matrix[row][col] == -1):
                self.matrix[row][col] = element
                element += 1
                row += 1
            self.print_matrix()

            while(col > -1 and self.matrix[row][col] == -1):
                self.matrix[row][col] = element
                element += 1
                col -= 1
            self.print_matrix()

            while(row > -1 and self.matrix[row][col] == -1):
                self.matrix[row][col] = element
                element += 1
                row -= 1
            self.print_matrix()
            col += 1
        return self.matrix


if __name__ == "__main__":
    n = 3
    obj = spiral_matrix(n)
    obj.generate_matrix()
    obj.print_matrix

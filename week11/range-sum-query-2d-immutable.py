#canbeimproved

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            for j in range(1,len(self.matrix[i])):
                
                self.matrix[i][j] = self.matrix[i][j-1] + self.matrix[i][j]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sumr = 0
        for i in range(row1, row2+1):
            sumr += self.matrix[i][col2] - (self.matrix[i][col1-1] if col1 >0 else 0)
        return sumr


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

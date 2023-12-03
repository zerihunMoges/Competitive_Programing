class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(1,len(matrix[i])):
                matrix[i][j] += matrix[i][j-1]
        self.matrix = matrix
        
    def update(self, row: int, col: int, val: int) -> None:
        dif = val - (self.matrix[row][col] - (self.matrix[row][col-1] if  col > 0 else 0))
    
        for j in range(col, len(self.matrix[row])):
            
            self.matrix[row][j] += dif
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        total = 0
        for i in range(row1, row2+1):
            total += self.matrix[i][col2] - (self.matrix[i][col1-1]  if col1 > 0 else 0)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
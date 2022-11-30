class Solution:
    def inBound(self, row, col, board):
        return 0 <= row < len(board) and 0 <= col < len(board[row])
    
    def isValid(self, row, col, queen, board):


        for i in range(len(board)):

            if board[i][col] == queen:
                return False  
            if self.inBound(row-i, col-i, board) and board[row-i][col-i] == queen:
                return False
            if self.inBound(row-i, col+i, board) and board[row-i][col+i] == queen:
                return False

        return True

    def placeQueens(self, board, queen, row):
        if row >= len(board):
            return 1

        ways = 0
        for col in range(len(board[row])):
            if self.isValid(row, col, queen, board):
                board[row][col] = queen
                ways += self.placeQueens(board, queen, row+1)
                board[row][col] = '.'

        return ways

    
    def totalNQueens(self, n: int) -> int:
        queen = 'Q'
        board = [['.' for i in range(n)] for j in range(n)]
        row = 0
        
        ways = self.placeQueens(board, queen, row)
        return ways
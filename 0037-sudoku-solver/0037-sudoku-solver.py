class Solution:
    def isValid(self, row, col, num, board):
        
        for i in range(len(board)):
            
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
            
            cur_row = row - row%3 + i//3
            cur_col = col - col%3 + i - (i//3)*3

            if board[cur_row][cur_col] == num:
                return False
        
        return True
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                
                if board[row][col] == '.':
                    nums = "123456789"
                    for num in nums:
                        
                         if self.isValid(row, col, num, board): 
                            board[row][col] = num
                            if self.solveSudoku(board):
                                return True
                            
                            board[row][col] = '.'
                            
                    return False
                
                elif row == len(board)-1  and col == len(board[row])-1:
                    return True
                        
                        
                
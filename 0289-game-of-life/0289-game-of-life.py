class Solution:
    def inBound(self, row, col, board):
        return 0 <= row < len(board) and 0 <= col < len(board[row])
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [ [1,0],[0,1],[1,1],[-1,-1],[-1,1], [1,-1],[0,-1],[-1,0]]
        
        neighbours = [[0]*len(board[0]) for i in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                for row, col in directions:
                    
                    new_row, new_col = i + row, j + col
                    
                    if self.inBound(new_row, new_col, board) and board[new_row][new_col] == 1:
                        neighbours[i][j] += 1
                        
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if neighbours[i][j] < 2 or neighbours[i][j] > 3:
                    board[i][j] = 0
                elif neighbours[i][j] == 3:
                    board[i][j] = 1
                    
        
        
        
        
        
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        dirt = [[-1,0],[0,-1],[0,1],[1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
        bound = lambda x,y: 0<= x < len(board) and 0<= y < len(board[0])
        def play(row,col):
            if board[row][col] == "E":
                count = 0
                for i in dirt:
                    nrow,ncol = row+i[0],col+i[1]
                    if bound(nrow,ncol):
                        if board[nrow][ncol] == "M":
                            count += 1
                            
                board[row][col] = "B" if count == 0 else str(count)

                for i in dirt:
                    nrow,ncol = row+i[0],col+i[1]
                    if bound(nrow,ncol) and board[row][col] == "B":
                        if board[nrow][ncol] == "E":
                            play(nrow,ncol)
                
    
        if board[click[0]][click[1]]== "M":
            board[click[0]][click[1]] = "X"
        else:
            play(click[0],click[1])
        
        return board

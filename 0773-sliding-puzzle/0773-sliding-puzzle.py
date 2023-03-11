class Solution:
    def inBound(self, row, col, board):
        return 0 <= row < len(board) and 0 <= col < len(board[row])
    def isComplete(self, board):
        return board == [[1,2,3],[4,5,0]]
#     def minMoves(self, pos, board, directions, visited):
        
# #         if self.isComplete(board):
# #             return 0
# #         b = tuple(board[0]+board[1])
# #         print(b)
# #         if b in visited:
# #             return float('inf')
        
        
        
# #         visited.add(b)
# #         minscore = float('inf')
# #         for rowd, cold in directions:
            
# #             newr, newc = pos[0]+rowd, pos[1] + cold
# #             if self.inBound(newr, newc, board):
# #                 board[pos[0]][pos[1]], board[newr][newc] = board[newr][newc],board[pos[0]][pos[1]]
# #                 minscore = min(1+self.minMoves( (newr, newc), board, directions, visited), minscore)
# #                 board[pos[0]][pos[1]], board[newr][newc] = board[newr][newc],board[pos[0]][pos[1]]

#         return minscore
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        position = (None, None)
        for row in range(len(board)):
            for col in range(len(board[row])):
                
                if board[row][col] == 0:
                    position = (row, col)
        

          
        visited = set()
        q = deque([[position, board]])
        level = 0
        while q:
            size = len(q)
            for i in range(size):
                pos, board = q.popleft()
                if self.isComplete(board):
                    return level
            
                
                
                for rowd, cold in directions:

                    newr, newc = pos[0]+rowd, pos[1] + cold
                    if self.inBound(newr, newc, board):
                        board[pos[0]][pos[1]], board[newr][newc] = board[newr][newc],board[pos[0]][pos[1]]
                        b = tuple(board[0]+board[1])
                        if b not in visited:
                            visited.add(b)
                            q.append([[newr, newc], [list(board[0]), list(board[1])]])
                        board[pos[0]][pos[1]], board[newr][newc] = board[newr][newc],board[pos[0]][pos[1]]
            level+=1
            
        return  -1
                
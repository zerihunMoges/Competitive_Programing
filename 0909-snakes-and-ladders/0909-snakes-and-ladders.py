class Solution:
    def findRow(self, current, n):
        row = (n-1) - (current-1)//n 
        col = (current-1)%n 
        if ((current-1)//n) % 2 != 0:
                col = (n-1)-col
                
        return row, col
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        

        cells = deque([[0,1]])
        visited = set()
        n = len(board)
        while cells:
            step, current = cells.popleft()
            row, col = self.findRow(current, n)
            if current == n**2:
                return step
            
            for j in range(current+1, min(n**2+1, current+7)):
                new_row, new_col = self.findRow(j, n)
                if board[new_row][new_col] != -1:
                    if board[new_row][new_col] not in visited:
                        visited.add(board[new_row][new_col])
                        cells.append([step+1, board[new_row][new_col]])
                elif j not in visited:
                    visited.add(j)
                    cells.append([step+1, j])
                    
                
                    
        return -1
class Solution:
    def isBorder(self, row, col, maze):
        if min(row,col) == 0 or row == len(maze)-1 or col == len(maze[row])-1:
            return True
        
    def inBound(self, row, col, maze):
        if row < 0 or row >= len(maze):
            return False
        return 0 <= col < len(maze[row])
    
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        cells = deque([entrance])
        entrance_row, entrance_col = entrance
        visited = set((entrance_row, entrance_col))
      
        level = 0
        while cells:
            size = len(cells)
            
            for i in range(size):
                row, col = cells.popleft()
                if self.isBorder(row, col, maze) and [row,col] != entrance:
                    return level
                
                for row_dirc, col_dirc in directions:

                    new_row = row + row_dirc
                    new_col = col + col_dirc

                    if self.inBound(new_row, new_col, maze) and (new_row, new_col) not in visited and maze[new_row][new_col] != '+': 
                        visited.add((new_row, new_col))
                        cells.append([new_row, new_col])
                        
            level += 1
                    
        return -1
            
            
            
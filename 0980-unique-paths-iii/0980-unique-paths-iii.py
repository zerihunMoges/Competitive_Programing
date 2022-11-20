class Solution:
    def inBound(self, row, col, grid):
        if row >= len(grid) or row < 0:
            return False
        
        return col < len(grid[row]) and col >= 0
    
    def findPath(self, row, col, visited, directions, grid, blocks):
       
        if grid[row][col] == 2 and len(visited) == len(grid)*len(grid[row]) - blocks -1:
            return 1
        
        visited.add((row, col))
      
        paths = 0
        for row_dirc, col_dirc in directions:
            new_row = row + row_dirc
            new_col = col + col_dirc
            
            if self.inBound(new_row, new_col, grid) and (new_row, new_col) not in visited and grid[new_row][new_col] != -1:
                paths += self.findPath(new_row, new_col, visited, directions, grid, blocks)
                
        visited.remove((row, col))
        
        return paths
        
                
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        visited = set()
        
        blocks = 0
        start_row = None
        start_col = None
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    start_row = row
                    start_col = col
                elif grid[row][col] == -1:
                    blocks += 1
                    
        
        return self.findPath(start_row, start_col, visited, directions, grid, blocks)
        
    
        
        
        
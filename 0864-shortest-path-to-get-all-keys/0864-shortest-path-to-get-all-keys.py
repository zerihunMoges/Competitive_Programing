class Solution:
    def isInBound(self, row, col, grid):
        if not 0 <= row < len(grid):
            return False
        return 0 <= col < len(grid[row])
    
    def shortestPathAllKeys(self, grid: List[str]) -> int:
    
        keys = 0
        start = None
    
        for row in range(len(grid)):
            
            for col in range(len(grid[row])):
                if grid[row][col] == '@':
                    start = [row, col]
                elif ord('a') <= ord(grid[row][col]) <= ord('z'):
                    keys += 1
                
        directions = [[0,-1], [1,0], [0,1],[-1,0]]
        cells = deque([[start, 0]])
        visited = set()
        level = 0
        
        while cells:
            
            for size in range(len(cells)):
                
                pos, foundKeys = cells.popleft()
                row , col = pos
                if ord('a') <= ord(grid[row][col]) <= ord('z'):
                    foundKeys = foundKeys | (1 << (ord(grid[row][col])-ord('a')))
                    if (1 << keys) -1 == foundKeys:
                        return level
                
                for row_dir, col_dir in directions:
                    new_row = row + row_dir
                    new_col = col + col_dir
                    
                    if self.isInBound(new_row, new_col, grid) and (new_row, new_col, foundKeys) not in visited and grid[new_row][new_col] != '#':
                        
                        if ord('A') <= ord(grid[new_row][new_col]) <= ord('Z'):
                            if foundKeys & (1 << (ord(grid[new_row][new_col])-ord('A'))):
                                visited.add((new_row, new_col, foundKeys))
                                cells.append([[new_row, new_col], foundKeys])
                        else:
                            visited.add((new_row, new_col, foundKeys))
                            cells.append([[new_row, new_col], foundKeys])
            level += 1
        return -1
                
                
        
                
class Solution:
    def inBound(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        visited = set()
        cells = deque()
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        for i in range(len(isWater)):
            for j in range(len(isWater[i])):
                
                if isWater[i][j]:
                    visited.add((i,j))
                    cells.append([i,j, 0])
       
        while cells:
            row, col, value = cells.popleft()
            isWater[row][col] = value
            
            for rd, cd in directions:
                if self.inBound(row+rd, col+cd, isWater) and (row+rd, col+cd) not in visited:
                    visited.add((row+rd, col+cd))
                    cells.append([row+rd, col + cd, value+1])
                    
        return isWater
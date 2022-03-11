class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        obstacles = 0
        
        start = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    obstacles += 1
                if grid[i][j] == 1:
                    start = [i,j]
                    
        inbound = lambda x,y: 0 <= x < len(grid) and 0 <= y < len(grid[0])           
        dirc = [[0,1],[1,0],[0,-1],[-1,0]]
        self.count = 0
        def dfs(row,col):
            nonlocal visited
            if grid[row][col] == 2 and len(visited) + obstacles  >= len(grid)*len(grid[0]):
                self.count += 1
                return 
            
            elif grid[row][col] == 2:
                return 
            
            for i in dirc:
                nposx = row+i[0]
                nposy = col+i[1]
                if (nposx, nposy) not in visited and inbound(nposx,nposy) and grid[nposx][nposy] != -1:
                    visited.add((nposx, nposy))
                    dfs(nposx,nposy)
                    visited.remove((nposx, nposy))
                    
        visited = set()
        visited.add((start[0],start[1]))
        dfs(start[0],start[1])
        
        return self.count

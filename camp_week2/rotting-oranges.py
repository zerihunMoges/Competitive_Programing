from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirt = [[-1,0],[0,-1],[0,1],[1,0]]
        visited = set() 
        inbound = lambda r,c: 0<=r<len(grid) and 0<= c<len(grid[0])
        soranges = deque()
        newsp = deque()
        empty = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    soranges.append([i,j])
                    visited.add((i,j))
                elif grid[i][j] == 0:
                    empty += 1
        time = 0
        while soranges or newsp:
            if newsp:
                time += 1
            while newsp:
                soranges.append(newsp.popleft())
            
            while soranges:
                orange = soranges.popleft()
                row = orange[0]
                col = orange[1]
                visited.add((row,col))
                for i in dirt:
                    nrow,ncol = row+i[0],col+i[1]
                    if inbound(nrow,ncol) and (nrow,ncol) not in visited and grid[nrow][ncol] != 0:
                        visited.add((nrow,ncol))
                        newsp.append([nrow,ncol])
        
        if len(visited) + empty == len(grid)*len(grid[0]):
            return time
        
        return -1

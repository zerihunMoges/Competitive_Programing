import heapq
from collections import deque

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirt = [[-1,0],[0,-1],[0,1],[1,0]]
        inbound = lambda r,c: 0<=r<len(grid) and 0<= c<len(grid[0])
        
        pools = []
        path = deque()
        visited = set()
        
        lowest = None
        time = grid[0][0]
        
        path.append([0,0])
        while path:
            curpos = path.popleft()
            visited.add((curpos[0],curpos[1]))
            for i in dirt:
                nrow = curpos[0] + i[0]
                ncol = curpos[1] + i[1]
                
                if inbound(nrow,ncol) and (nrow, ncol) not in visited:
                    heapq.heappush(pools, [grid[nrow][ncol], [nrow,ncol]])
            
            if [curpos[0],curpos[1]] == [len(grid)-1, len(grid[0])-1]:
                break
            
            lowest = heapq.heappop(pools)
            time = max(time,lowest[0])
            path.append(lowest[1])
                            
        return time

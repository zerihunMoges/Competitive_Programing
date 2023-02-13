class Solution:
    def inBound(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        q =deque([])
        if grid[0][0] == 0:
            q.append([0,0])
        visited = set()
        ds = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        level = 1
        while q:
            
            for i in range(len(q)):
                r, c = q.popleft()
                
                if r == len(grid)-1 and c == len(grid[r])-1:
                    return level
                for r_d, c_d in ds:
                    n_r = r + r_d
                    n_c = c + c_d
                    
                    if self.inBound(n_r, n_c, grid) and (n_r, n_c) not in visited and grid[n_r][n_c] == 0:
                        visited.add((n_r, n_c))
                        q.append([n_r, n_c])
                
            level += 1
                
        return -1
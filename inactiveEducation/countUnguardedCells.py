class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        
        visited = set()
        wall = set()
        for w in walls:
            wall.add((w[0], w[1]))
        guard = set()
        for g in guards:
            guard.add((g[0], g[1]))
        directions = [[0,1],[1,0],[0,-1], [-1,0]]  
        guards = guard
        inbound = lambda x,y: 0 <= x < m and 0 <= y < n
        
        for g in guards:
            cur = g
            for d in directions:
                x,y = cur[0]+d[0], cur[1]+d[1]
                while inbound(x, y) and (x,y) not in wall and (x,y) not in guards:

                    visited.add((x,y))
                    
                    x,y = x+d[0], y+d[1]
                    
        return m*n - len(visited) - len(guards) - len(walls)
                 
            
        
    

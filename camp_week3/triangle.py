class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        self.dp = {}
        def mini(x,y):
            if x == len(triangle)-1:
                return triangle[x][y]
            if (x,y) in self.dp:
                return triangle[x][y] + self.dp[(x,y)]
            minp = mini(x+1,y)
            minp1 = mini(x+1, y+1)
            
            self.dp[(x,y)] = min(minp, minp1)
            return triangle[x][y] + self.dp[(x,y)]
        
        return mini(0,0)

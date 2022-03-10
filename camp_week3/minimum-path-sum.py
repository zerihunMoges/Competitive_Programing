class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp = {}
        def minimum(x,y):
            print(x,y)
            if x == len(grid)-1 and y == len(grid[0])-1:
                return grid[x][y]
            if (x,y) in self.dp:
                return grid[x][y] + self.dp[(x,y)]
            
            if x == len(grid)-1:
                self.dp[(x,y)] = minimum(x, y+1)
                return  grid[x][y] + self.dp[(x,y)]
            elif y == len(grid[0]) - 1:
                self.dp[(x,y)] = minimum(x+1, y)
                return  grid[x][y] + self.dp[(x,y)]
            
            else:
                self.dp[(x,y)] = min(minimum(x+1,y), minimum(x, y+1))
                return  grid[x][y] + self.dp[(x,y)]
        return minimum(0,0)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirt = [[-1,0],[0,-1],[0,1],[1,0]]
        visited = set()
        inbound = lambda x,y: 0 <= x < len(grid) and 0<= y< len(grid[0])
        
        def walk(row,col):
            if (row,col) not in visited:
                visited.add((row,col))
                for i in dirt:
                    nrow,ncol = row+i[0], col+i[1]
                    
                    if inbound(nrow,ncol) and grid[nrow][ncol] == 1 and (nrow,ncol) not in visited:
                        walk(nrow,ncol)
        
        
        #only border
        def right(row, column):
            for i in range(column):
                if grid[0][i] == 1:
                    walk(0, i)
                if grid[row - 1][i] == 1:
                    walk(row - 1, i)

        def down(row, column):
            for i in range(row):
                if grid[i][0] == 1:
                    walk(i, 0)
                if grid[i][column - 1] == 1:
                    walk(i, column - 1)
                    
                    
        row = len(grid)
        col = len(grid[0])
        right(row,col)
        down(row,col)
        
        count = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j] == 1 and (i,j) not in visited:
                    count += 1
                    
        return count

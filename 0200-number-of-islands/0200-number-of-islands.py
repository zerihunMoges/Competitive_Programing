class Solution:
    def inBound(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])
    
    def find(self,row, col, root):
        if root[row][col] == (row, col):
            return root[row][col]
        
        parent_row, parent_col = root[row][col]
        root[row][col] = self.find(parent_row, parent_col, root)
        return root[row][col]
    
    def union(self ,row_x,col_x, row_y, col_y, rank, root):
        rootx = self.find(row_x,col_x, root)
        rooty = self.find(row_y, col_y, root)
        x_row, x_col = rootx
        y_row, y_col = rooty
        
        if rootx != rooty:
            if rank[x_row][x_col] > rank[y_row][y_col]:
                root[y_row][y_col] = rootx
            elif rank[x_row][x_col] < rank[y_row][y_col]:
                root[x_row][x_col] = rooty
            else:
                root[y_row][y_col] = rootx
                rank[x_row][x_col] += 1
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        root = [[(i,j) for j in range(len(grid[i]))] for i in range(len(grid))]
        
        rank = [[0]*len(grid[i]) for i in range(len(grid))]
        
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                
                if grid[row][col] == "1":
                    for row_dirc, col_dirc in directions:
                        new_row, new_col = row+row_dirc, col+col_dirc
                        
                        if self.inBound(new_row, new_col, grid) and grid[new_row][new_col] == "1":
                            self.union(row, col, new_row, new_col, rank, root)
        
        visited = set()

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    parent = self.find(row, col, root)
                    if parent not in visited:
                        islands += 1
                        visited.add(parent)
                    
        return islands
        
        
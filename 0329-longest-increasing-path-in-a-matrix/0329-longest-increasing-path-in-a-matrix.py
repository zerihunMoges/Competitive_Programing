class Solution:
    def inBound(self, row, col , matrix):
        return 0 <= row < len(matrix) and 0<= col < len(matrix[row])
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        directions = [[-1,0],[0,1],[1,0],[0,-1]]
        less_count = defaultdict(int)
        max_length = defaultdict(int)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                
                for row_dir, col_dir in directions:
                    new_row = i + row_dir
                    new_col = j + col_dir
                
                    if self.inBound(new_row, new_col, matrix):
                        if matrix[new_row][new_col] < matrix[i][j]:
                            less_count[(i,j)] += 1
        nums = deque()           
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                max_length[(i,j)] = 1
                if less_count[(i,j)] == 0:
                    nums.append([i,j , 1])
                
        
        while nums:
            
            row, col, length = nums.popleft()
            
            
            for row_dir, col_dir in directions:
                new_row = row + row_dir
                new_col = col + col_dir
                
                if self.inBound(new_row, new_col, matrix):
                    if matrix[new_row][new_col] > matrix[row][col]:
                        less_count[(new_row,new_col)] -= 1
                        max_length[(new_row,new_col)] = max(max_length[(new_row,new_col)], length+1)
                        
                        if less_count[(new_row,new_col)] == 0:
                            nums.append([new_row,new_col, max_length[(new_row,new_col)]])
                
            
            
        return max(max_length.values())
                    
                    
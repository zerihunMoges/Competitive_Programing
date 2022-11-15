class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        max_size = 0
        for i in range( len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
            
                if matrix[i][j] == 1:
                    extends = 0
                    if j > 0 and i > 0:
                        extends = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
                        
                    matrix[i][j] = extends+1
                    max_size = max(matrix[i][j], max_size)
                    
        return max_size**2
                    
            
                    
                
    
        
        
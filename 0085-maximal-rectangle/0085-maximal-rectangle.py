class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_rectangle = 0
        for row in range(len(matrix)):
            heights = []
           
            for col in range(len(matrix[row])):
                matrix[row][col] = int(matrix[row][col])
                if row > 0 and matrix[row][col] == 1:
                    matrix[row][col] += matrix[row-1][col]
                    
                while heights and matrix[row][heights[-1]] > matrix[row][col]:
                    larger = heights.pop()
                    left = -1
                    if heights:
                        left = heights[-1]
                    max_rectangle = max(matrix[row][larger]*(col-left-1), max_rectangle)
                
                    
                heights.append(col)

                
            while heights:
                larger = heights.pop()
                left = -1
                if heights:
                    left = heights[-1]
                max_rectangle = max(matrix[row][larger]*(len(matrix[row])-left-1), max_rectangle)

        return max_rectangle
                    
                    
        













        
        
        
        
        
        
        
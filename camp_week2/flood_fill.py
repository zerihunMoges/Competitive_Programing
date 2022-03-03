class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dirt = [[-1,0],[0,-1],[0,1],[1,0]]
        color = image[sr][sc]
        if newColor == color:
            return image
        
        def fill(sr,sc):
            image[sr][sc] = newColor
            for i in dirt:
                row = sr+i[0]
                col = sc+i[1]
                if row >= 0 and col >= 0 and  row < len(image) and col < len(image[0]):
                        if image[row][col] == color:
                            fill(row,col)
                            
        fill(sr,sc)
        
        return image
                      

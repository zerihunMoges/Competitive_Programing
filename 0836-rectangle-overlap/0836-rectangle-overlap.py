class Solution:
    def lineOverlap(self, line1, line2):
        
        lines = [line1, line2]
        
        lines.sort()
        line1 = lines[0]
        line2 = lines[1]
        
        return line1[1] > line2[0]
    
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        
        return self.lineOverlap([rec1[0], rec1[2]], [rec2[0], rec2[2]]) and self.lineOverlap([rec1[1], rec1[3]] ,[rec2[1] ,rec2[3]])
    
    
  
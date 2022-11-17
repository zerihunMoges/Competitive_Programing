class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        area1 = abs(ax1-ax2)*abs(ay1-ay2)
        area2 = abs(bx1-bx2)*abs(by1-by2)
       
        xoverlap = 0
        yoverlap = 0
        
        left = max(ax1, bx1)
        right = min(bx2, ax2)
        if right > left:
            xoverlap = right - left
        
        top = min(by2, ay2)
        bottom = max(ay1, by1)
        if top > bottom:
            yoverlap = top - bottom 
            
        total = area1+area2 - xoverlap*yoverlap
        return total
        
        
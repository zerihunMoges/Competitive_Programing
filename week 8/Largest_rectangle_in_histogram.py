class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        his = []
        maxarea = 0
        
        for i in range(len(heights)):
            while his and  heights[i] < heights[his[-1]]:
                poped = his.pop()
                left = his[-1]+1 if his else 0

                area = heights[poped]*( i - left)
                maxarea = max(maxarea, area)
                
            his.append(i)

        while his:

            poped = his.pop()
            left = his[-1]+1 if his else 0
            
            area = heights[poped]*( len(heights) - left)
            maxarea = max(maxarea, area)    



        return maxarea

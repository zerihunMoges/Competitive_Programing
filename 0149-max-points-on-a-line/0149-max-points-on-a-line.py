class Solution:
    def maxPointsLine(self, prevx, prevy, ydif, xdif, points, memo):
        
        if (prevx, prevy, ydif, xdif) in memo:
            return memo[(prevx, prevy, ydif, xdif)]
        
        max_points = 0
        for x,y in points:
            new_ydif = prevy-y
            new_xdif = prevx-x
           
            if (prevx > x or (prevx == x and prevy > y)) and (ydif == None or (new_ydif*xdif == ydif*new_xdif)):
                points_count = 1 + self.maxPointsLine(x, y, new_ydif, new_xdif, points, memo) 
                max_points = max(max_points, points_count)
                
        memo[(prevx,prevy, ydif, xdif)] = max_points
        
        return memo[(prevx,prevy, ydif, xdif)]
        
        
    def maxPoints(self, points: List[List[int]]) -> int:
        
        memo = defaultdict(int)
        max_points = 0 
        for x,y in points:
            points_count = 1+self.maxPointsLine(x,y, None, None, points, memo)
            
            max_points = max(points_count, max_points)
       
        # 1,2,3
        
        
        return max_points
        
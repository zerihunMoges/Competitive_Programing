class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        left = 1
        right = max(dist)*100
        minSpeed = float('inf')
        while left <= right:
            mid = (left+right)//2
            time = 0
            for train in dist:
                time = math.ceil(time)
                time += train/mid
                
            
            if time <= hour:
                minSpeed = mid
                right = mid-1
            else:
                left = mid+1
                
                
        return minSpeed if minSpeed < float('inf') else -1
            
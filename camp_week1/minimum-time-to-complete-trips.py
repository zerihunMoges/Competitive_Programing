class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        btime = None
        left = 1
        right = min(time)*totalTrips
        
        while left <= right:
            mid = (left+right)//2
            trip = 0
            for i in range(len(time)):
                trip += mid//time[i]
                
            if trip >= totalTrips:
                right = mid-1
                btime = mid
            else:
                left = mid+1
                
        return btime

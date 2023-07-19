class Solution:
   
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort(key = lambda interval: interval[1])
        
        prevstart, prevend = -float('inf'), -float('inf')
        removed = 0
    
        for curstart, curend in intervals:
            if prevend <= curstart:
                prevstart, prevend = curstart, curend
            else:
                removed += 1
                
        return removed
            
            
            
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        def findNext(start):
            
            left = 0
            right = len(events)-1
            best = len(events)
            while left <= right:
                mid = (left+right)//2
                if events[mid][0] < start:
                    left = mid+1
                else:
                    best = mid
                    right = mid-1
                    
            return best
                    
                
        @lru_cache(maxsize=None)
        def sol(i, l):
            if l == k or i >= len(events):
                return 0
            
            pick = events[i][2] + sol(findNext(events[i][1]+1), l+1)
            skip = sol(i+1, l)
            
            return max(pick, skip)
        
        return sol(0, 0)
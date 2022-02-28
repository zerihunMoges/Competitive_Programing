import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        jumps = []
        
        i = 0
        while i < len(heights)-1:
            if heights[i+1]-heights[i]>0:
                
                if bricks - (heights[i+1]-heights[i]) >= 0:
                    bricks -= heights[i+1]-heights[i]
                    heapq.heappush(jumps,-1*(heights[i+1]-heights[i]))
                
                elif ladders > 0:
                    if jumps != [] and -1*jumps[0] > heights[i+1]-heights[i]:
                        bricks -= heapq.heappop(jumps)
                        ladders -= 1
                        i-=1
                    else:
                        ladders -= 1    
                else:
                    return i
                
            i+=1
            
        return len(heights)-1
        

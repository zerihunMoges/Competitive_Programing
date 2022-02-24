import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)): 
            stones[i] = -1*stones[i]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            fb = -1*heapq.heappop(stones)
            sb = -1*heapq.heappop(stones)
            
            if fb != sb:
                heapq.heappush(stones, sb-fb)
        
                
        return -1*stones[0] if len(stones)==1 else 0
                

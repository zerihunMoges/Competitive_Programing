class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        need = []
        for i in range(len(capacity)):
            heapq.heappush(need, capacity[i]-rocks[i])
            
        while need and additionalRocks - need[0] >= 0:
            additionalRocks -= heapq.heappop(need)
            
        return len(capacity) - len(need)
            
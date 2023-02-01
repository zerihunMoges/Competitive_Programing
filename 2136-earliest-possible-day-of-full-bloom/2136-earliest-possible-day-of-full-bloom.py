class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        
        
        plants = []
        
        for i in range(len(growTime)):
            heapq.heappush(plants, [-growTime[i], plantTime[i], i])
        
        plant_time = 0
        time_max = 0
        while plants:
            time, ptime, i = heapq.heappop(plants)
            
            plant_time += plantTime[i]
            
            time_max = max(time_max, plant_time-time)
           
        return time_max
    

            
        
            
        
        
        
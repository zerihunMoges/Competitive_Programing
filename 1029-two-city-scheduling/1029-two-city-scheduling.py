class Solution:
    
    def schedule(self, person, available, costs, memo):
        
        if person >= len(costs):
            return 0
        
        if (person, available) in memo:
            return memo[(person, available)]
        citya = float('inf')
        cityb = float('inf')
        if available > 0:
            
            citya = costs[person][0] + self.schedule(person+1, available-1, costs, memo)
        if  person - (len(costs)//2 - available) < len(costs)//2 :
            cityb = costs[person][1] + self.schedule(person+1, available, costs, memo)
        
        memo[(person, available)] = min(citya, cityb)
        return memo[(person, available)]
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        memo = defaultdict(int)
        
        return self.schedule(0, len(costs)//2, costs, memo)
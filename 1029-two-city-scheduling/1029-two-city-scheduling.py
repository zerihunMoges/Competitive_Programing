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
      
        
        diff = []
        for i in range(len(costs)):
            costa, costb = costs[i]
            diff.append([abs(costa-costb), i])
        size = len(costs)//2
        diff.sort(reverse=True)
        citya = 0
        cityb = 0
        tot = 0
        
        for i in range(len(diff)):
            dif, index = diff[i]
            
            if costs[index][0] < costs[index][1]:
                if citya < size:
                    tot += costs[index][0]
                    citya += 1
                else:
                    tot += costs[index][1]
                    cityb+=1
            else:
                if cityb < size:
                    tot += costs[index][1]
                    cityb+=1
                else:
                    tot += costs[index][0]
                    citya += 1
                    
        return tot
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
        citya = []
        cityb = []
        
        for i in range(len(diff)):
            dif, index = diff[i]
            
            if costs[index][0] < costs[index][1]:
                if len(citya) < size:
                    citya.append(costs[index][0])
                else:
                    cityb.append(costs[index][1])
                    
            else:
                if len(cityb) < size:
                    cityb.append(costs[index][1])
                else:
                    citya.append(costs[index][0])
        
        return sum(citya)+sum(cityb)
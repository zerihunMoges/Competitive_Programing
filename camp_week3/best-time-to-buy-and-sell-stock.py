
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for idx in range(2, len(cost)):
            
            cost[idx] = min(cost[idx-1], cost[idx-2]) + cost[idx]
            
        return min(cost[-1], cost[-2])
    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp = {}
        def minCost(i, c):
            
            if i > len(cost)-1:
                return c
            if i in self.dp:
                return c+self.dp[i]
            
            else:
                v= min(minCost(i+1, cost[i]),minCost(i+2, cost[i]))
                self.dp[i] = v
                return c+v
        
        return min(minCost(1, 0), minCost(0, 0))

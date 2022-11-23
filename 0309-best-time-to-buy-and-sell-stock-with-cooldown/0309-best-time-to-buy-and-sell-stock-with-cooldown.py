class Solution:
    def getMaxProfit(self, haveStock, day, memo, prices):
        if day >= len(prices):
            return 0
        
        if (day, haveStock) in memo:
            return memo[(day, haveStock)]
        
        if haveStock:
            memo[(day, haveStock)] = max(prices[day] + self.getMaxProfit(not haveStock, day+2, memo, prices), self.getMaxProfit(haveStock, day+1, memo, prices))
        else:
            memo[(day, haveStock)] = max(-prices[day] + self.getMaxProfit(not haveStock, day+1, memo, prices), self.getMaxProfit(haveStock, day+1, memo, prices))
        
        return memo[(day, haveStock)]
             
        
    def maxProfit(self, prices: List[int]) -> int:
        
       
        states = 2
        day = 0
        memo = [[0]*(states) for i in range(len(prices)+2)]
        for day in reversed(range(len(memo)-2)):
            for state in range(states):
                
                if state == 0:
                    memo[day][state] = max(-prices[day] + memo[day+1][state+1], memo[day+1][state])
                else:
                    memo[day][state] = max(prices[day] + memo[day+2][state-1], memo[day+1][state])
             
        return memo[0][0]
                    
                    
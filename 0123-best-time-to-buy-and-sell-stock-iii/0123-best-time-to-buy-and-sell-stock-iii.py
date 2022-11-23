class Solution:
  
        
    def maxProfit(self, prices: List[int]) -> int:
        transactions = 2
        states = 2
        
        memo = [[[0]*(transactions+1) for i in range(states)] for j in range(len(prices)+1)]
        
        
        
        for day in reversed(range(len(memo)-1)):
            for state in range(len(memo[day])):
                for transaction in range(1, len(memo[day][state])):
                    if state == 1:
                        memo[day][state][transaction] = max(prices[day]+memo[day+1][state-1][transaction-1], memo[day+1][state][transaction] )
                        
                    else:
                        memo[day][state][transaction] = max(-prices[day]+memo[day+1][state+1][transaction], memo[day+1][state][transaction] )
        
        
        return max(memo[0][0])
                        
       
        
        
        
        
        
        
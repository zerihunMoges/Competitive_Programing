class Solution:
  
        
    def maxProfit(self, prices: List[int]) -> int:
        transactions = 2
        states = 2
        
        memo = [[0]*(transactions+1) for i in range(states)]
        
        
        
        for day in reversed(range(len(prices))):
            for state in range(len(memo)):
                for transaction in range(1, len(memo[state])):
                    if state == 1:
                        memo[state][transaction] = max(prices[day]+memo[state-1][transaction-1], memo[state][transaction] )
                        
                    else:
                        memo[state][transaction] = max(-prices[day]+memo[state+1][transaction], memo[state][transaction] )
        
        
        return max(memo[0])
                        
       
        
        
        
        
        
        
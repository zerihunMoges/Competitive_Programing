class Solution:
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
                    
                    
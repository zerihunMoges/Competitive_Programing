class Solution:
    def findMaxProfit(self, haveStock, transactions, day, prices, memo):
        if transactions >= 2 or day >= len(prices):
            return 0
        if (haveStock, transactions, day) in memo:
            return memo[(haveStock, transactions, day)]
        if haveStock:
            sell = prices[day] + self.findMaxProfit(not haveStock, transactions+1, day+1, prices, memo)
            keep = self.findMaxProfit(haveStock, transactions, day+1, prices, memo)
            memo[(haveStock, transactions, day)] = max(keep, sell)
        else:
            buy = -prices[day] + self.findMaxProfit(not haveStock, transactions, day+1, prices, memo)
            idle = self.findMaxProfit(haveStock, transactions, day+1, prices, memo)
            memo[(haveStock, transactions, day)] = max(buy, idle)
            
        return memo[(haveStock, transactions, day)]
        
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
                        
       
        
        
        
        
        
        
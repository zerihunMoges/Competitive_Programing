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
        memo = defaultdict(int)
        haveStock = False
        transactions = 0
        day = 0
        
        profit = self.findMaxProfit(haveStock, transactions, day, prices, memo)

                 
        
        return profit
        
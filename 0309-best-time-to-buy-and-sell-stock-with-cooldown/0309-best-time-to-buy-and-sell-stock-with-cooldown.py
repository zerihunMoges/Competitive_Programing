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
        
        haveStock = False
        day = 0
        memo = defaultdict(int)
        return self.getMaxProfit(haveStock, day, memo, prices)
class Solution:
    def sol(self, prices, idx, hasStock, memo):
            
        if idx >= len(prices):
                return 0
        if (idx, hasStock) in memo:
            return memo[(idx, hasStock)]
        
        buy = 0
        sell = 0
        if not hasStock:
            buy = -prices[idx] + self.sol(prices, idx+1, not hasStock, memo)
            
        if hasStock:
            sell = prices[idx] + self.sol(prices, idx+1, not hasStock, memo)
            
        skip = self.sol(prices, idx+1, hasStock, memo)
        
        memo[(idx, hasStock)] = max(buy, sell, skip)
        
        return memo[(idx, hasStock)]
    
    def maxProfit(self, prices: List[int], idx=0, hasStock = False) -> int:
        
        memo = defaultdict(int)
        return self.sol(prices, idx, hasStock, memo)
        
        
        
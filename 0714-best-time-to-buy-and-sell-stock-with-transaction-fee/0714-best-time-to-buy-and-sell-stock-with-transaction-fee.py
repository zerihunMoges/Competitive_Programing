class Solution:
    def maxProfit(self, prices: List[int], fee: int, bought=False, i=0) -> int:
        
        memo=defaultdict(int)
        
        def sol(prices, fee, bought, i, memo):
            if i >= len(prices):
                return 0
            if (bought, i) in memo:
                return memo[(bought, i)]
            buy = 0
            sell = 0
            if not bought:
                buy = -prices[i]-fee +  sol( prices, fee, True, i+1, memo)
            else:
                sell = prices[i] + sol( prices, fee, False, i+1, memo)

            skip = sol( prices, fee, bought, i+1, memo)

        
            memo[(bought, i)] = max(buy, sell, skip)
            return memo[(bought, i)]
    
        return sol(prices, fee, False, 0, memo)
class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        
        dp = [0]*(n+2)
        dp[1] = 1

        for i in range(2, len(dp)):
            
            dp[i] = dp[i-1]+dp[i-2]
       
        return dp[-1]
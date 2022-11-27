class Solution:
    @lru_cache(maxsize=None)
    def countWays(self, n , prev):
        
        if n == 0:
            return 1
        ways = 0
        if not prev:
            ways += self.countWays(n-1, not prev) 
            
        
        
        return ways + self.countWays(n-1, False)
    
    def countHousePlacements(self, n: int) -> int:
        ways = self.countWays(n, False)
        
        
        return (ways**2)%(10**9+7)
        
        




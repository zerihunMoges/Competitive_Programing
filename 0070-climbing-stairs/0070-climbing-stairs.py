class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        
        
        prev, prev_prev = 1, 0

        for i in range(n):
            temp = prev
            prev = prev + prev_prev
            
            prev_prev = temp
       
        return prev
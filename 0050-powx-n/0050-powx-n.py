class Solution:
    @lru_cache(maxsize=None)
    def myPow(self, x: float, n: int) -> float:
        if n < -1 or n > 1:
            return self.myPow(x ,n//2)*self.myPow(x, n//2 + n%2)
        elif n == 1:
            return x
        elif n == 0:
            return 1
        elif n == -1:
            return 1/x
        
        
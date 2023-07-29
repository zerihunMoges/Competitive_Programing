class Solution:
    def soupServings(self, n: int) -> float:
        
        @lru_cache(maxsize=None)
        def sol(a, b):
            
            if a <= 0 and b <= 0:
                return 1/2
            
            if a <= 0:
                return 1
            
            if b <= 0:
                return 0
            
            
            return sum(sol(a-an, b-bn) for an, bn in [[100,0], [75, 25], [50, 50], [25,75]])/4
        return 1 if n > 4450 else sol(n,n)
            
            
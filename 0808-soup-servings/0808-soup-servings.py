class Solution:
    def soupServings(self, n: int) -> float:
        m = n//25 + min(1,n%25)
        @lru_cache(maxsize=None)
        def sol(a, b):
            
            if a <= 0 and b <= 0:
                return 1/2
            
            if a <= 0:
                return 1
            
            if b <= 0:
                return 0
            
            
            return sum(sol(a-an, b-bn) for an, bn in [[4,0], [3, 1], [2, 2], [1,3]])/4
        return 1 if n > 4450 else sol(m,m)
            
            
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        @lru_cache(maxsize=None)
        def sol(cur, fuel):
            if fuel < 0:
                return 0
            
    
            
            total = 0
            for i in range(len(locations)):
                if cur != i:
                    total += sol(i, fuel- (abs(locations[cur]-locations[i]))) 
                    
                    
            return total + (1 if cur == finish else 0)
        
        return sol(start, fuel)%(10**9+7)
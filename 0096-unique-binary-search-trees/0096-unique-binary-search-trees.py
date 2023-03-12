class Solution:
    def numTrees(self, n: int) -> int:
        
       
        @lru_cache(maxsize = None)
        def unique(num, left, right):
            
            if left > right:
                return 0 
            
            if num == right and num == left:
                return 1
            
            l = 0
            r = 0
            for i in range(num+1, right+1):
                l +=  unique(i, num+1, right)
            
            for i in range(num-1, left-1, -1):
                
                r +=  unique(i, left, num-1)

            return max(1, l)*max(1, r)
        
        return unique(0, 1, n)
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def ind(i, n):
            if i == 0:
                return 1
            if i == 1:
                return n
            
            result = ind(i//2, n)
            return (result*result*ind(i%2, n))%1000000007%1000000007
        
        return (ind(n//2 + n%2, 5)*ind(n//2, 4))%1000000007
        

class Solution:
    def fib(self, n: int) -> int:
        
        if n<=2:
            return int(n/2 + 0.5)
          
        return self.fib(n-2) + self.fib(n-1)
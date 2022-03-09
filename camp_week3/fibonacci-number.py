class Solution:
    def fib(self, n: int) -> int:
        def fibb(n):
            if n == 1 or  n == 0:
                return n
            
            if n in self.f:
                return self.f[n]
            else:
                r = fibb(n-1) + fibb(n-2)
                self.f[n] = r
                return r
            
        self.f = {}
        return fibb(n)

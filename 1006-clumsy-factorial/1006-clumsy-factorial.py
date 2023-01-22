class Solution:
    def clumsy(self, n: int) -> int:
        
        factorial = 0
        current= 0
        sign = 1
        for i in range(n):
            
            r = (i+1) %4
            if r == 0:
                current = current + (n-i)
                factorial += current
                
                current = 0
                sign = -1  
                
            elif r == 1:
                current = current + sign*(n-i)
                
                
            elif r == 2:
                current*=(n-i)
                
                
            elif r == 3:
                current= abs(current)//(n-i)//(abs(current)//current)
                
        
        return factorial + current
        
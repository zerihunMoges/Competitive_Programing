class Solution:
    def switch(self, num, i, numfinal):
        
        if i*2-1 == numfinal//2  :
            return num
        
        return (num)*self.switch((num*num)%1000000007, i*2, numfinal)
    
    def minNonZeroProduct(self, p: int) -> int:
        
        lastindex = pow(2,p) - 1
        mod = pow(10,9)+7
        if lastindex == 1:
            return lastindex
        
        return (self.switch(lastindex-1,1, lastindex-1)*lastindex % mod)

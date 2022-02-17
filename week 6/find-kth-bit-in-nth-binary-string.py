class Solution:
    def invert(self, s):
        inverted = ''
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                inverted += '1'
            else:
                inverted += '0'
        return inverted
    
    def toBinaryString(self, n):
        if n == 1:
            return '0'

        else:
            binary =  self.toBinaryString(n-1)
            
            return  (binary + "1" + self.invert(binary) )
        
    def findKthBit(self, n: int, k: int) -> str:
        
        return self.toBinaryString(n)[k-1]

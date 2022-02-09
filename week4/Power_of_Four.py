class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>4:
            return self.isPowerOfFour(n/(16))
        
        elif n==1 or n==4:
            return True
        
        elif n < 1:
            return False
        

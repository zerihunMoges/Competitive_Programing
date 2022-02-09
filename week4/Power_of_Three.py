class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n>3:
            return self.isPowerOfThree(n/(9))
        
        elif n==1 or n==3:
            return True
        
        elif n < 1:
            return False

class Solution:
    def checkRecord(self, s: str) -> bool:
        
        
        l = 0
        a = 0
        
        for i in range(len(s)):
            
            
            if s[i] == "A":
                a += 1
                l = 0
                
            elif s[i] == "L":
                l += 1
            else:
                l = 0
                
            if a >= 2 or l >= 3:
                return False
            
        return True
            
            
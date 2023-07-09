class Solution:
    def largestVariance(self, s: str) -> int:
        chars = set(s)
        best = 0
        for i in chars:
            for j in chars:
                
                
                if i != j:
                    prefix = 0
                    minm = 0
                    temp = None
                    
                    for k in range(len(s)):
                        if s[k] == i:
                            prefix += 1
                        elif  s[k] == j:
                            prefix -= 1
                            temp = minm
                            minm = prefix if prefix < minm else minm
    
                        best = max(prefix - temp, best) if temp != None else best
                    
                        
                        
        return best
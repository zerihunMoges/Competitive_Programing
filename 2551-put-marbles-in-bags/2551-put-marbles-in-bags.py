class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        
        
        
        
        border = []
        
        for i in range(len(weights)-1):
            border.append(weights[i]+weights[i+1])
            
        border.sort()
        difference = 0
        for i in range(k-1):
            difference += border[-i-1]
            difference -= border[i]
            
        return difference
        
            
            
            
       
        
        
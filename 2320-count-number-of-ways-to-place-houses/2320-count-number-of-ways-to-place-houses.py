class Solution:
   
    
    def countHousePlacements(self, n: int) -> int:
        
        ways = [[0,0] for i in range(n+1)]
        top = 1
        bottom = 1
        for i in range(1, len(ways)):
            tempt = 0
            tempb = 0
            for j in range(len(ways[i])):
                if j == 0:
                    tempt += bottom
                    tempt += top
                else:
                    tempb += top
            top = tempt
            bottom = tempb
                
        return (top**2)%(10**9+7)
        
        




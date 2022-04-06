class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        streak = 1
        tot = 0
        for i in range(len(prices)):
            if i>0:
                if prices[i-1] -prices[i] ==1:
                    streak += 1  
                else:
                    streak = 1
            tot += streak      
          
        
        return tot
                    

class Solution: 
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
     
        
        dp = [0]*(len(s1)+1)
        
        for i in range(len(s2)+1):
            prev = 0
            for j in range(len(s1)+1):
                cur_best = 0
                if 0 <= i+j-1 < len(s3):
                    
                    if j > 0 and s1[j-1] == s3[i+j -1]:
                        cur_best = max(cur_best, prev + 1)
                    
                    if i > 0 and s2[i-1] == s3[i+j -1]:
                        cur_best = max(cur_best, dp[j] + 1)
                  
                dp[j] = cur_best
                prev = cur_best
      
        return dp[-1] == len(s3)
     
        
     
        
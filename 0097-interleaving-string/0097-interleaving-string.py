class Solution: 
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
     
        
        dp = [[0]*(len(s1)+1) for i in range(len(s2)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[i])):

                if 0 <= i+j-1 < len(s3):
                    cur_best = 0
                    if j > 0 and s1[j-1] == s3[i+j -1]:
                        cur_best = max(cur_best, dp[i][j-1] + 1)
                    
                    if i > 0 and s2[i-1] == s3[i+j -1]:
                        cur_best = max(cur_best, dp[i-1][j] + 1)
                  
                    dp[i][j] = cur_best
                    
        for row in dp:
            print(row)
       
        return dp[-1][-1] == len(s3)
                
     
        
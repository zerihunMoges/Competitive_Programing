class Solution:
      
    def minCut(self, s: str) -> int:
        
        dp = [i for i in range(len(s)+1)]

        for i in range(len(s)*2-1):
           
            start = i//2
        
            left = start
            right = start + (i&1)
            
            while 0 <= left and right < len(s) and s[left] == s[right]:
                
                dp[right+1] = min(dp[right+1], dp[left] + 1)
                right +=1
                left -= 1
      
        return dp[-1] - 1
            
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = []
    
        
        for i in range(len(s)):
            k = 0
            while i-k > -1 and i+k < len(s) and s[i-k] == s[i+k]:
                
           
                
                l = [i-k, i+k] if l == [] or 2*k >= l[1]-l[0] else l
                k+=1
                
            k = 0
            while i-k > -1 and i+k+1 < len(s) and s[i-k] == s[i+k+1]:
                

                l = [i-k, i+k+1] if l == [] or 2*k+1 >= l[1]-l[0] else l
                k+=1
        return s[l[0]:l[1]+1]

class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rec(n):
            if n == 1:
                return '1'
            
            return count(rec(n-1))
     
        def count(s):
            ans = ''
            j = 0
            for i in range(len(s)):
                if s[i] != s[j]:
                    ans += str(i-j)+s[j]
                    j = i
                if i == len(s) -1:
                    ans += str(i-j+1)+s[i]

            return ans
        return rec(n)

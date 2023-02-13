class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [0]*(len(b)- len(a)) + list(map(int, list(a)))
        b = [0]*(len(a)- len(b)) + list(map(int, list(b)))
        
        have = 0
        ans = []
        for i in reversed(range(len(a))):
            
            cur = a[i] + b[i]
            
            cur += have
            
            if cur >= 2:
                have = 1
                
                ans.append(str(cur%2))
                
            else:
                have = 0
                ans.append(str(cur))
                
        if have:
            ans.append(str(have))
            
        return ''.join(reversed(ans))
            
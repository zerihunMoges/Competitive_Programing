class Solution:
    
    def minFlip(self, s, i, hasOne, memo):
        
        if i >= len(s):
            return 0
        
        if (i, hasOne) in memo:
            return memo[(i, hasOne)]
        
        flips = 0
        if hasOne:
            flips += 1-int(s[i]) + self.minFlip(s, i+1, hasOne, memo)
            
        else:
            
            flip = 1+self.minFlip(s, i+1, s[i] == '0', memo)
            keep = self.minFlip(s, i+1, s[i] == '1', memo)
            flips = min(flip, keep)
            
        memo[(i, hasOne)] = flips
        return memo[(i, hasOne)]
        
    def minFlipsMonoIncr(self, s: str) -> int:
        memo = defaultdict(int)
        return self.minFlip(s, 0,False, memo)
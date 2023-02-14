class Solution:
    
    def minD(self, i, hasb, s, memo):
        if i  >= len(s):
            return 0
        if (i, hasb) in memo:
            return memo[(i, hasb)]
        
        if hasb and s[i] == 'a':
            return 1+ self.minD(i+1, hasb, s, memo)
        
        memo[(i, hasb)] = min(self.minD(i+1, s[i] == 'b', s, memo), 1+ self.minD(i+1, hasb, s, memo))
        return memo[(i, hasb)]
        
            
    def minimumDeletions(self, s: str) -> int:
        
        return self.minD(0, False, s, defaultdict(int))
class Solution:
    
    def maxSubset(self, m,n, comb, idx, memo):
        if idx >= len(comb):
            return 0
        
        if (m,n,idx) in memo:
            return memo[(m,n,idx)]
        
        zero, one = comb[idx]
        pick  = 0
        skip = 0
        if zero <= m and one <= n:
            pick = 1+ self.maxSubset(m-zero, n-one, comb, idx+1, memo)
            
        skip = self.maxSubset(m, n, comb, idx+1, memo)
        
        memo[(m,n,idx)] = max(pick, skip)
        
        return memo[(m,n,idx)]
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        
        comb = []
        memo = defaultdict(int)
        for i in strs:
            
            comb.append([i.count('0'), i.count('1')])
                
        return self.maxSubset(m,n,comb, 0, memo)
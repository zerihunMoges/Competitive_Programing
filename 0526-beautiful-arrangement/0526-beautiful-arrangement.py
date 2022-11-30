class Solution:
    
    def findArrangement(self, idx, used, n , memo):
        if idx > n:
            return 1
        if (idx, used) in memo:
            return memo[(idx, used)]
        
        ways = 0
        for num in range(1, n+1):
            if not (1 << num)&used and (idx%num == 0 or num%idx == 0):
                
                ways += self.findArrangement(idx+1, used | (1 << num), n, memo)
        memo[(idx, used)] = ways   
        return ways  
    
    def countArrangement(self, n: int) -> int:
        memo = defaultdict(int)
        arrangements = self.findArrangement(1, 0, n, memo)
       
        return arrangements
   
    
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        
        count = defaultdict(int)
        tot = 0
        for t in time:
            
            for i in range(60, t+561, 60):
                tot += count[i-t]
            count[t] += 1
                
        return tot
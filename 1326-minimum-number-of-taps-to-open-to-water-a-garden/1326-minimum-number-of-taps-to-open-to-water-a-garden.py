class Solution:
    
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        mintap = [0] + [float('inf')] * n
        
        for i in range(len(ranges)):
            rng = ranges[i]
            for j in range(max(0, i+1 - rng), min(i + rng, n) + 1):
                mintap[j] = min(mintap[j], mintap[max(0, i - rng)] + 1)
                
        return mintap[n] if mintap[n] != float('inf') else -1
    
    
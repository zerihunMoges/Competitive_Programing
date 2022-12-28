class Solution:
    def maxJump(self, stones: List[int]) -> int:
        gap = stones[1]-stones[0]
        for i in range(2,len(stones)):
            gap = max(gap, stones[i]-stones[i-2])
                
                    
        return gap
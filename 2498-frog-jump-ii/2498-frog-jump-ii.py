class Solution:
    def maxJump(self, stones: List[int]) -> int:
        gap = stones[1]-stones[0]
        for i in range(len(stones)-1):
            if i%2 == 0:
                if i+2 < len(stones):
                    gap = max(gap, stones[i+2]-stones[i])
                else:
                    gap = max(gap, stones[i+1]-stones[i])
            else:
                if i+2 < len(stones):
                    gap = max(gap, stones[i+2]-stones[i])
                else:
                    gap = max(gap, stones[i+1]-stones[i])
                    
        return gap
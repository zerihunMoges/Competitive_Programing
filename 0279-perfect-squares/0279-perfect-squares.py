
class Solution:
    memo = defaultdict(int)
    def minSquares(self, idx, cur, nums, memo):
        
        if cur == 0:
            return 0
        elif cur < 0 or idx >= len(nums):
            return float('inf')
        
        if (idx, cur) in memo:
            return memo[(idx, cur)]
        
        pick = 1+ min(self.minSquares(idx+1, cur-nums[idx], nums, memo), self.minSquares(idx, cur-nums[idx], nums, memo))
        skip = self.minSquares(idx+1, cur, nums, memo)
        
        memo[(idx, cur)] = min(pick , skip)
        
        return memo[(idx, cur)]
    
    def numSquares(self, n: int) -> int:
        memo = self.memo
        nums = [ i**2 for i in range(1, 101)]
        return self.minSquares(0, n, nums, memo)
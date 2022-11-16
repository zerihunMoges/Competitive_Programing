class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        
        @lru_cache(maxsize = None)
        def ans(i, s):
            
            if s == tot//2:
                return True
            if i == len(nums):
                return False
            
            return ans(i+1, s-nums[i]) or ans(i+1, s)
        return ans(0,tot) if tot%2 ==0 else False
            
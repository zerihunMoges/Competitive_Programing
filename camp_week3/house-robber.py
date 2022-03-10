class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dp = {}
        def robhouse(i):
            
            if i >= len(nums) - 1:
                return nums[i] if i == len(nums)-1 else 0
            if i in self.dp:
                return nums[i] + self.dp[i]
            self.dp[i] = max(robhouse(i+2), robhouse(i+3))
            return nums[i] + self.dp[i]
        
        return max(robhouse(0),robhouse(1))

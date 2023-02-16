class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pastm = 0
        curm = -float('inf')   
        for i in range(len(nums)):
            nums[i] += nums[i-1] if i > 0 else 0
            
            curm = max(nums[i]-pastm, curm)
            pastm = min(pastm, nums[i])

        return curm
class Solution:
    def maxSum(self, i, nums):
        if i >= len(nums):
            return 0, 0, 0
        
        
        mx, mi, glo = self.maxSum(i+1, nums)
        
        return max(nums[i], mx+nums[i]), min(nums[i], mi+nums[i]) , max(abs(nums[i]), abs(nums[i]+mx), abs(nums[i]+mi), glo)
    
    
    
        
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        return self.maxSum(0, nums)[2]
        
    
        
        
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        
        m = nums[0]
        maxd = -1
        for i in range(len(nums)):
            
            if m < nums[i]:
                maxd = max(maxd, nums[i]-m)
                
            else:
                m = nums[i]
                
                
        return maxd
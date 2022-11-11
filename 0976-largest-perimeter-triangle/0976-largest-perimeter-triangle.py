class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        
        nums.sort()
        
        
        for i in reversed(range(2, len(nums))):
            highest = nums[i]
            
            second, third = nums[i-1], nums[i-2]
            if second+third > highest:
                return second+third+highest
            
        return 0
            
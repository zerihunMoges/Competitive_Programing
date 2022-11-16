class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.append(0)
        max_pos = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > max_pos-1:
                nums[i] = 0
                
        for i in range(len(nums)):
            
            nums[nums[i]%len(nums)] += max_pos
            
        for i in range(1, len(nums)):
            if nums[i]//max_pos == 0:
                return i
            
            
        return max_pos
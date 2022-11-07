class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        
        j = len(nums)-1
        for i in range(len(nums)):
            
            while j > i and nums[j] != 0:
                j -= 1
                
            if j > i and nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                
        j = len(nums)-1
        for i in range(len(nums)):
            
            while j > i and nums[j] != 1:
                j -= 1
                
            if j > i and nums[i] == 2:
                nums[i], nums[j] = nums[j], nums[i]
                
        
            
            

        
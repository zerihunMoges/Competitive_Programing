class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[j] != 0:
                j+=1
            elif nums[i] != 0:
                nums[j], nums[i] = nums[i],nums[j]
                j+=1
        

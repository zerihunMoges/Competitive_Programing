class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] and nums[i]< nums[i-1]:
                nums[i] , nums[i+1] = nums[i+1], nums[i]
            elif nums[i] < nums[i+1] and nums[i] > nums[i-1]:
                nums[i] , nums[i+1] = nums[i+1], nums[i]
       
        return nums 

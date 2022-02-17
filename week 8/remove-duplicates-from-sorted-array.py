class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        i = 1
        while i < len(nums):
            if nums[j] == nums[i]:
                i+=1
            else:
                nums[j+1], nums[i] = nums[i],nums[j+1]
                i+=1
                j+=1
            
            
        return j+1

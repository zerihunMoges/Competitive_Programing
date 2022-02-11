class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        i = 1
        while i < len(nums):
            if nums[j] == nums[i]:
                nums.pop(i)
                i-=1
            else:
                j+=1
            i+=1
            
        return len(nums)

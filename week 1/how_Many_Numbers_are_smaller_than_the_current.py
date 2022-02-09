
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednum = sorted(nums)
        for i in range(len(nums)):
            nums[i] = sortednum.index(nums[i])
            
        return nums

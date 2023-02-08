class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) <=2:
            return nums[-1]
        return nums[-3]
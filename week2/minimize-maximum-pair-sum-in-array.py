class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maximum = nums[0] + nums[-1]
        for i in range(len(nums)//2):
            numsum =  nums[i] + nums[-i-1]
            maximum = numsum if numsum > maximum else maximum
        return maximum

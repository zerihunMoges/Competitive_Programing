class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        nums.add(0)
        return len(nums)-1
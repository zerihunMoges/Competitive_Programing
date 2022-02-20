class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum = [0]*len(nums)
        prefixsum[0] = nums[0]
        for i in range(1,len(nums)):
            prefixsum[i] += nums[i]+prefixsum[i-1]
        pivot = -1
     
        for i in range(len(prefixsum)):
            left =   prefixsum[i-1] if i != 0 else 0
            right = prefixsum[len(prefixsum)-1] - prefixsum[i] if i != len(prefixsum)-1 else 0
            if left == right:
                return i
                
        return pivot

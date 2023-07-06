class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0 
        min_l = 0
        j = 0
        for i in range(len(nums)):
            
            cur_sum += nums[i]
            
            while cur_sum >= target and j <= i:
                min_l = i-j+1 if min_l == 0 or  min_l > i-j+1 else min_l
                cur_sum -= nums[j]
                j += 1
                
        return min_l
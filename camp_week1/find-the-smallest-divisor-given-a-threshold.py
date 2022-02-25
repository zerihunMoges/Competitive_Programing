from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        
        left = 1
        right = max(nums)
        bestdiv = 0
        while  left <= right:
            mid = (left+right)//2
            total = 0
            for i in range(len(nums)):
                total += ceil(nums[i]/mid)
                
            if total > threshold:
                left = mid+1
                
            elif total <= threshold:
                right = mid-1
                bestdiv = mid
                
        return bestdiv
                

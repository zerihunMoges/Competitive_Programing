class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = min(nums)
        right = max(nums)
        pd = None
        while left <= right:
            mid=(left+right)//2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count +=1
                    
            if count > mid:
                right = mid-1
                pd = mid
                
            elif count <= mid:
                left = mid+1
                
        return pd

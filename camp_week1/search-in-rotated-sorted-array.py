class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums)-1
        pl = None
        
        while left <= right:
            
            mid = (left+right)//2
            if nums[mid] > nums[len(nums)-1]:
                left = mid+1
            elif nums[mid] < nums[len(nums)-1]:
                right = mid-1
                pl = mid
            else:
                pl = mid
                break
        
        if nums[len(nums)-1] >= target:
            left = pl
            right = len(nums)-1
        else:
            left = 0
            right = pl-1
         
        while left<= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid +1
            else:
                return mid
        return -1
            

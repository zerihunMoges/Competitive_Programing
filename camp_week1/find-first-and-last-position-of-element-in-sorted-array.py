class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums)-1
        br = -1
        while left <= right:
            
            mid = (left+right)//2
            
            if nums[mid] == target:
                br = mid
            if nums[mid] <= target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
                
        left = 0
        right = len(nums)-1   
        
        bl = -1
        
        while left <= right:
            
            mid = (left+right)//2
            
            if nums[mid] < target:
                left = mid+1
                
                    
            elif nums[mid] >= target:
                right = mid-1
                if nums[mid] == target:
                    bl = mid
            
        return [bl, br]

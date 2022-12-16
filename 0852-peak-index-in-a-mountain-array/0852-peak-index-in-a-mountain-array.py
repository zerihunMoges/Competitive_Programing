class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        left = 1
        right = len(arr)-2
        
        while left <= right:
            
            
            mid = (left+right)//2
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            
            elif arr[mid] < arr[mid+1]:
                left = mid+1
                
            elif arr[mid] < arr[mid-1]:
                right = mid-1
                
        
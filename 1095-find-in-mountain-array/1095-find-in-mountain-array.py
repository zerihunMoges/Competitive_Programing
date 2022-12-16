# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findCenter(self, mountain, left, right):
        
        
        while left <= right:
            
            
            mid = (left+right)//2
            
            east = mountain.get(mid+1)
            center = mountain.get(mid)
            west = mountain.get(mid-1)
            if west < center > east:
                return mid
            
            elif center < east:
                left = mid+1
                
            elif center < west:
                right = mid-1
            
    def findLeft(self, mountain, target, left, right):

        while left <= right:
            
            
            mid = (left+right)//2
            center = mountain.get(mid)
            
            if center < target:
                left = mid+1
                
            elif center > target:
                right = mid-1
                
            else:
                return mid
            
        return -1
    
    def findRight(self, mountain, target, left, right):
        
        while left <= right:
            
            
            mid = (left+right)//2
            center = mountain.get(mid)
            
            if center < target:
                right = mid-1
            
            elif center > target:
                left = mid+1
                
            else:
                return mid
            
        return -1
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left = 1
        right = mountain_arr.length()-1
        center = self.findCenter(mountain_arr, left, right-1)
        
        l = self.findLeft(mountain_arr, target, 0, center)
        if l != -1:
            return l
        
        r = self.findRight(mountain_arr, target, center+1, right)
        return r
        
        
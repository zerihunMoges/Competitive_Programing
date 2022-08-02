class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        result = 0
        curm = 0
        left =[0]*len(height)
        right = [0]*len(height)
        
        for i in range(len(height)):
            curm = max(curm,height[i])
            left[i]=curm
         
        curm=0
        for i in range(len(height)-1,-1,-1):
            curm = max(curm,height[i])
            right[i]=curm
            
        
        volume = 0
        for i in range(len(height)):
            
            volume += max(min(left[i],right[i])-height[i], 0)
            
        return volume

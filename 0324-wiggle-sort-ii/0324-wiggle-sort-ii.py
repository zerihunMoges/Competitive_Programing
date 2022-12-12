class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        order = sorted(nums)
        i = len(order)//2 -1 + len(order)%2
        j = len(order)-1
        print(order)
        for k in range(0,len(nums),2):
            
            nums[k] = order[i]
            
            if  k+1 < len(order):
                nums[k+1] = order[j]
            
            i-=1
            j-=1
            
      
            
        
        
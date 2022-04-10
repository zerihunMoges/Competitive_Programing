class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        count = 0
        start =0
        temp = nums[(-k)%len(nums)]
        while count < len(nums):
            if i%len(nums) == start:
                start += 1
                temp = nums[(i+1-k)%len(nums)]
                i+=1
            ntemp = nums[(i)%len(nums)]
            nums[(i)%len(nums)] = temp
            temp = ntemp                
            i+=k
            
            count += 1

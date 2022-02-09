class Solution:
    def sortColors(self, nums: List[int]) -> None:
        j= 0
        i = 0
        leng = len(nums)
        while i < leng:
            if nums[i] == 2:
                nums.append(nums.pop(i))
                i-=1
                leng -= 1
            elif nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j+=1
            i+=1
		

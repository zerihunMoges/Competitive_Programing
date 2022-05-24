class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
       
        nums[0] = nums[0]%2
        for i in range(1, len(nums)):
            nums[i] = nums[i]%2 + nums[i-1]

        j=-1
        
        i =0
        count = 0
        while i < len(nums):
            
            end = i
            while i < len(nums) and nums[i] - (nums[j] if j >=0 else 0) == k:
                i += 1
                if i >= len(nums) or nums[i] - (nums[j] if j >=0 else 0) != k:
                    i-=1
                    break
            i+=1
            start = j
            while nums[i-1] - (nums[j] if j >=0 else 0) == k:
                j+=1
            count += (j-start)*(i-end)
            
        return count

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        maxim = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                
                if(i-firstLen+1 > j or j-secondLen+1  > i) and i >= firstLen-1 and j >= secondLen-1:
        
                    firstsum = nums[i]- (nums[i-firstLen] if i-firstLen >= 0 else 0)
                    secondsum =  nums[j]- (nums[j-secondLen] if j-secondLen >= 0 else 0)

                    maxim = max(firstsum+secondsum, maxim)
                    
        return maxim

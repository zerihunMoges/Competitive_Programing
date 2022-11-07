class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = [0] + nums
      
        for i in range(1,len(sums)):
            sums[i] += sums[i-1]

        for i in range(1,len(sums)):
            
            if sums[i-1] == sums[-1] - sums[i]:
                return i-1
        
      
        return -1
        
        
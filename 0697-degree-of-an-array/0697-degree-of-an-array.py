class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        
        shortest = None
        count = defaultdict(list)
        for num in range(len(nums)):
            count[nums[num]].append(num)
            
            cl = count[nums[num]][-1]-count[nums[num]][0]+1
            if shortest == None or len(count[shortest]) < len(count[nums[num]]) or (count[shortest][-1]-count[shortest][0]+1 > cl and  len(count[shortest]) == len(count[nums[num]])):
                shortest = nums[num]
                
        return count[shortest][-1]-count[shortest][0]+1 
        
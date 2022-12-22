class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        
            count = Counter(nums)
            prev = None
            available = []
            temp = []
            for i in reversed(range(len(nums))):
                
                
                if i < len(nums)-1 and nums[i] != nums[i+1]:
                    if available and available[0] < 3:
                        return False
                    available = temp
                    temp = []
                    prev = nums[i+1]
                    
                if available and prev == nums[i]+1:
                    cur = heapq.heappop(available)
                    heapq.heappush(temp, cur+1)
                else:
                    heapq.heappush(temp, 1)
                    
            while temp and temp[0] >= 3:
                heapq.heappop(temp)
                
            return temp == []
                
            
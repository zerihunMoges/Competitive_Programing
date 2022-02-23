import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        fre = {
        }
        for i in range(len(nums)):
            if nums[i] in fre:
                fre[nums[i]] += 1
            else:
                fre[nums[i]] = 1
                
        
        freq = []
        
        for i in fre:
            freq.append([-1*fre[i], i])
        heapq.heapify(freq)
        
        klargest = []
        for i in range(k):
            klargest.append(heapq.heappop(freq)[1])
            
        return klargest
    

class Solution:
    def maximumSwap(self, num: int) -> int:
        
        nums = []
        num = list(map(int, list(str(num))))
        for i in range(len(num)):
            heapq.heappush(nums, [-num[i], -i])
            
        want = []
        front = 0
        while nums:
            cur, idx= heapq.heappop(nums)
            
            if num[front] < -cur:
                num[front], num[-idx] = num[-idx], num[front]
                
                return int(''.join(map(str, num)))
            heapq.heappush(nums, [cur, idx])
            while nums and -nums[0][1] <= front:
                heapq.heappop(nums)
                
            front += 1
            
        return int(''.join(map(str, num)))    
        
        
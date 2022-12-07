from sortedcontainers import SortedList 

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
       
        sl, ans = SortedList(), []      
        
        
        for i in reversed(range(len(nums))):
            sl.add(nums[i])
            count = sl.bisect_left(nums[i])
            
            ans.append(count)
            
        return reversed(ans)
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        values = defaultdict(int)
        
    
        
        def rec(i, cur):
            
            if i  == len(nums):
                values[cur] += 1
                return 
            
            rec(i+1, cur|nums[i])
            rec(i+1, cur)
            
            
        rec(0,0)

        return values[max(values)]
        

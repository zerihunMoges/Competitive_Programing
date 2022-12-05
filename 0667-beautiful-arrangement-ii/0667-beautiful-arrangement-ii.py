class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
    
        
        nums = set([i for i in range(2, n+1)])
        
        ans = [1]
        for i in reversed(range(1,k+1)):
            if (ans[-1]-i) in nums:
                nums.remove(ans[-1]-i)
                ans.append(ans[-1]-i)
                
            elif (ans[-1]+i) in nums:
                nums.remove((ans[-1]+i))
                ans.append(ans[-1]+i)
                
        return ans + sorted(nums)
            
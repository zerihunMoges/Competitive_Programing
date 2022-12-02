class Solution:
    
    def findPermutation(self, n,  target, idx, available, prev):
        if idx < 0:
            return ''
        cur = math.factorial(idx)+prev
        nums = sorted(available)
        i = 0
        while cur < target:
            
            cur += math.factorial(idx)
            i += 1
            
        available.remove(nums[i])
        return str(nums[i]) + self.findPermutation(n, target, idx-1, available, cur-math.factorial(idx))
    
        
    def getPermutation(self, n: int, k: int) -> str:
        
        perm = self.findPermutation(n, k, n-1, set([i for i in range(1, n+1)]), 0)
        return perm
        
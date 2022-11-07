class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        pos = [0 for _ in range(len(nums))]
        
        path = []
        ans = []
        def sol():
            if len(path) == len(nums):
                ans.append(list(path))
                return 
            
            for i in range(len(nums)):
                if pos[i] != 1:
                    pos[i] = 1
                    path.append(nums[i])
                    sol()
                    path.pop()
                    pos[i] = 0
                
        sol()
        return ans
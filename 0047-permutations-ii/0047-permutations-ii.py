class Solution:
    
    def permute(self, nums, permutation, length):
        if len(permutation) == length:
            return [list(permutation)]
        
        permutations = []
        for num in nums:
            if  nums[num] > 0:
                permutation.append(num)
                nums[num] -= 1
                permutations.extend(self.permute(nums, permutation, length))
                nums[num] += 1
                permutation.pop()
        
        return permutations
                
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums = Counter(nums)
        permutation = []
        return self.permute(nums, permutation, length)
        
        
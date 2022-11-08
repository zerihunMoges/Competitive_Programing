class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        
        current_xor = 0
    
        for num in nums:
            current_xor ^= num
        nums = set(nums)
       
        uniques = []
        possible = []
        for num in nums:

            if num^current_xor in nums:
                if num == 0 or num^current_xor == 0:
                    possible.append(num)
                else:
                    uniques.append(num)
                    
        if uniques:
            return uniques
        
        return possible
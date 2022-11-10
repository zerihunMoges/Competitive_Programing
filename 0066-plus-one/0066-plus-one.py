class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        have = 1
        
        for i in reversed(range(len(digits))):
            
            result = digits[i] + have
            have = 0
            have = (result - result%10)//10
            digits[i] = result%10
            
        if have:
            digits.insert(0, have)
            
        return digits
                
        
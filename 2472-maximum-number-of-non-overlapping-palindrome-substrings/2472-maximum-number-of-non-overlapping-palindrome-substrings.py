class Solution:
    def compare(self, left, right,s,  palindromes, k):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right-left + 1 >= k:   
                palindromes[right] = max(palindromes[left-1] + 1, palindromes[right-1], palindromes[right])
            else:
                palindromes[right] = max(palindromes[left-1], palindromes[right])
                
            left -= 1
            right += 1
            
    def maxPalindromes(self, s: str, k: int) -> int:
        
        palindromes = [0]*(len(s)+1)
        
        for i in range( len(s)):
            self.compare(i,i, s, palindromes, k)
            self.compare(i,i+1,s, palindromes, k)

        return palindromes[-2]
            
            
        
        
        
        
        
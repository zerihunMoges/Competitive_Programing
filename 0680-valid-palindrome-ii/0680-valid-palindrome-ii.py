class Solution:
    def isPalindrome(self, s):
       
        return s[:len(s)//2] == ''.join(reversed(s[len(s)//2+len(s)%2:])) or len(s) == 1
    def validPalindrome(self, s: str) -> bool:
        palindrome = True
        skipped = False
        j = len(s)-1
        for i in range(len(s)//2):
            
            if s[i] != s[j]:
                return self.isPalindrome(s[i:j]) or self.isPalindrome(s[i+1: j+1])
            
            j -= 1
        return True
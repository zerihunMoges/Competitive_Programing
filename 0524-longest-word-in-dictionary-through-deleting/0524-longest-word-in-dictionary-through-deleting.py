class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        
        dictionary.sort()
        maxLength  = ''
        
        for word in dictionary:
            
            j = 0
            for i in range(len(s)):
                if j < len(word) and s[i] == word[j]:
                    j+=1
                    
            if j == len(word) and len(maxLength) < len(word):
                
                    maxLength = word
                    
        return maxLength
                
                
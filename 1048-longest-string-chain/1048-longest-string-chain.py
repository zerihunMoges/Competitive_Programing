class Solution:
    def isPre(self, s, l):
        found = False
        if len(s) == len(l)-1:
            j = 0
            i = 0
            while i < len(s) and j < len(l):
                if s[i] != l[j]:
                    i-=1
                
                j+=1
                i+=1
        
            return i == len(s)
              
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key = lambda x: len(x))
        
        ln = [0]*len(words)
        
        for i in reversed(range(1, len(words))):
            for j in reversed(range(i)):
                if self.isPre(words[j], words[i]):
                    ln[j] = max(ln[j], ln[i]+1)
         
        return max(ln) + 1
            
                    
        
                    
                    
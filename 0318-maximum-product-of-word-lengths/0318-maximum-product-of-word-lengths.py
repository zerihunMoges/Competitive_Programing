class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        
        length = defaultdict(int)
        new_words = []
        
        for word in words:
            n = 0
            for letter in word:
                n |= 1 << ord(letter)-ord('a')
                
            new_words.append(n)
            
        max_length = 0
        letters = [ chr(ord('a')+i) for i in range(ord('a'), ord('z')+1)]
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                
                if not (new_words[i]&new_words[j]):
                    
                    max_length = max(max_length, len(words[i])*len(words[j]))
                    
        return max_length
                
        
                
            
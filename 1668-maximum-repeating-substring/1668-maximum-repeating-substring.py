class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        
        
        
        max_length = 0
        for i in range(len(sequence)):
            j  = 0 
            for k in range(i, len(sequence)):
                j = j%len(word)
                

                if sequence[k] != word[j]:
                    
                    break
                max_length = max((k-i + 1)//len(word), max_length)
                j+=1
        return max_length
                
        
        
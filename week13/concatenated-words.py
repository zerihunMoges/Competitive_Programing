class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordl = set(words)
        
        answer = set()             
        def rec(i,j, word):
            if word in answer:
                return
            
            if word not in wordl:
                wordl.add(word)
            
            if  j >= len(word):
                if word[i:j] in wordl and i != 0:
                    answer.add(word)
                else:
                    return 
            
            if word[i:j] in wordl:
                rec(j, j+1, word)
                
            rec(i, j+1, word)
                
        for i in words:
            rec(0,1, i)
            
        return list(answer)

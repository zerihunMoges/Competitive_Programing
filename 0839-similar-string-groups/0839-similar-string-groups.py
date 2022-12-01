class Solution:
    def similar(self, word1, word2):
        difference = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                difference += 1
            if difference > 2:
                return False
                
        return difference == 0 or difference == 2
    
    def findSimilar(self, word, visited, strs):
        
        words = deque([word])
        visited.add(word)
        
        while words:
            word = words.popleft()
            for new_word in strs:
                if self.similar(new_word, word) and new_word not in visited:
                    visited.add(new_word)
                    words.append(new_word)
                
                          
    def numSimilarGroups(self, strs: List[str]) -> int:
       
        group = 0
        visited = set()
        
        for word in strs:
            if word not in visited:
                group += 1
                self.findSimilar(word, visited, strs)
                
                
        return group
            
            
            
            
        
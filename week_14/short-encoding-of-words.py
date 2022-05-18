class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        trie = defaultdict(set)
            

        
        words.sort(key=lambda x: len(x) , reverse = True)
        print(words)
        
#         trie = defaultdict(set)
        
#         length = defaultdict(int)
        branch = 0
        for word in words:
            
    
            cur = trie
            change = 0
            for i in range(len(word)-1, -1,-1):
                
                if word[i] not in cur:
                    cur[word[i]] = defaultdict(set)
                    change = len(word)+1
                    
                    
                cur = cur[word[i]]
            branch += change
        return branch

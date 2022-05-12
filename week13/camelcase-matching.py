class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        trie = defaultdict(set)
        
        cur = trie
        
        for i in pattern:
            if i not in cur:
                cur[i] = defaultdict(set)
                
                
            cur = cur[i]
            
            
        answer = []
    
        for word in queries:
            cur = trie
            l = 0
            while l < len(word):
                if word[l] not in cur and 65 <= ord(word[l]) <= 90:
                    
                    break 
                elif word[l] in cur:
                    cur = cur[word[l]]
                l+=1
            if len(cur) == 0 and l == len(word):
                answer.append(True)
            else:
                answer.append(False)
            
            
        return answer

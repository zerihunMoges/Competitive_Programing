class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = defaultdict(set)
        longest = ''
        for word in words:
            cur = trie
            isCon = True
            for i in range( len(word)):
                
                if word[i] not in cur:
                    if i != len(word)-1:
                        isCon = False
                        break
                        
                    cur[word[i]] = defaultdict(set)
            
                cur = cur[word[i]]
            if isCon:
                longest = word if len(word) > len(longest) else longest
        
        
        return longest

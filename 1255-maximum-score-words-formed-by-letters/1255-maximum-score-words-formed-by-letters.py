class Solution:
    def maxScore(self, word, words, letters, score):
        
        if word >= len(words):
            return 0
        
        create = 0
        cur = Counter(words[word])
        
        if all([ letters[let] >= cur[let] for let in cur ]):
            s = 0
            for let in cur: 
                letters[let] -= cur[let]
                s += cur[let]*score[ord(let)-ord('a')]
            create = s + self.maxScore(word+1, words, letters, score)
            for let in cur: 
                letters[let] += cur[let]
        skip = self.maxScore(word+1, words, letters, score)
        
        return max(create, skip)
                      
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        
        letters = Counter(letters)
        return self.maxScore(0, words, letters, score)
        
        
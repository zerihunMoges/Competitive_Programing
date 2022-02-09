class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        sortedList = [0]*(len(s))
        for i in range(len(s)):
            sortedList[int(s[i][-1])-1] = s[i][:-1]
            
        return (' '.join(sortedList))
            

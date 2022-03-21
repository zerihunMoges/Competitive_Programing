
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = {}
        for i in range(len(s)):letters[s[i]] = i
            
        pos,lastpos,answer = 0,-1,[]
        for i in range(len(s)):
            pos = max(letters[s[i]], pos)
            if i == pos:
                answer.append(pos-lastpos)
                lastpos = pos
          
        return answer
    
###########################################    
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = {}
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        
        dupl = 0
        current = 0
        vis = set()
        answer = []
        for i in range(len(s)):
            if s[i] not in vis:
                dupl += 0 if letters[s[i]] <=1 else letters[s[i]]
                vis.add(s[i])
            if letters[s[i]] > 1:
                dupl -= 1
                
            current += 1
            if dupl == 0:
                answer.append(current)
                current = 0
                
        return answer

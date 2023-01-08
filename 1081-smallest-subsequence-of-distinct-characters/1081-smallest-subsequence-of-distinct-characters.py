class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        
        
        indexes = defaultdict(list)
        for i in range(len(s)):
            indexes[s[i]].append(i)
            
            
        answer = []
        in_answer = [False]*26
        for i in range(len(s)):
            
            if not in_answer[ord(s[i])-ord('a')]:
                while answer and answer[-1] >= s[i] and indexes[answer[-1]][-1] > i:
                    letter = answer.pop()
                    in_answer[ord(letter)-ord('a')] = False
                    
                answer.append(s[i])
                in_answer[ord(s[i])-ord('a')] = True

        return ''.join(answer)
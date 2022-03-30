class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        strings = set()
        answer = set()
        if len(s) >= 10:
            for i in range(len(s)-9):
                window = s[i:i+10]
                if window in strings:
                    answer.add(window)
                strings.add(window)
                
        return list(answer)

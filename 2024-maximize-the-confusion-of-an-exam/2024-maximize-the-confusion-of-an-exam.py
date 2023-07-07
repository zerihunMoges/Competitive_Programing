class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        best = 0
        
        check = ['T', 'F']
        for value in check:
            j = 0
            change = 0
            for i in range(len(answerKey)):
                change += 1 if answerKey[i] != value else 0
                while change > k and j < i:
                    change -= 1 if answerKey[j] != value else 0
                    j += 1
                best = max(best , i -j +1)
                
        return best
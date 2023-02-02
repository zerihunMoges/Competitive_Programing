class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digits = []
        
        letters = []
        
        for log in logs:
            l = log.split()
            
            if l[1].isdigit():
                digits.append(log)
                
            else:
                letters.append([l[1:], l[0]])
                
        letters.sort()
        
        return [ idn+' '+' '.join(letter) for letter, idn in letters] + digits
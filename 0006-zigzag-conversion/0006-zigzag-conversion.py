class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        row = [[] for _ in range(numRows)]
        direction = True
        c = 0
        i = 0
        for i in range(len(s)):
            row[c].append(s[i])
            if direction == True:
                c+=1
                if c >= numRows-1:
                    c = numRows-1
                    direction = False
            elif direction == False:
                c-=1
                if c <= 0:
                    c = 0
                    direction = True
            
            
        return ''.join([num for sublist in row for num in sublist])
                
            
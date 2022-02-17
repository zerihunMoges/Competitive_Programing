from curses.ascii import isdigit

class Solution:
    def decode(self, s, i, brackets):
        if i >= len(s):
            return s
        elif isdigit(s[i]):
            j = s.index('[', i)
            digit = ''.join(s[i:j])
            
            s[i:j] = [int(digit)]
            brackets.append(i+1)
            return self.decode(s, i+1,brackets)
        
        elif len(brackets) == 0:
            return self.decode(s, i+1,brackets)
        
        elif s[i] == ']':
            
            j = brackets.pop(-1)
            r = s[j-1]
            s[j-1:i+1] =  r* s[j+1:i]
            return self.decode(s, j-1+ (r)*(i-j-1),brackets)
        
        return self.decode(s, i+1,brackets)

    
    def decodeString(self, s: str) -> str:
        bracket =[]
        return ''.join(self.decode(list(s), 0, bracket))
        

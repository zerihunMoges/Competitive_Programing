class Solution:
    def decodeString(self, s: str) -> str:
        
        
        current = 0
        multipliers = []
        decoded = []
        for i in range(len(s)):
            
            if s[i].isdigit():
                current = current*10 + int(s[i])
                
            elif s[i] != ']':
                if s[i] == '[':
                    multipliers.append(current)
                decoded.append(s[i])
    
                current = 0
            else:
                d = ''
                while decoded and decoded[-1] != '[':
                    d = decoded.pop()+d
                    
                decoded.pop()
                decoded.append(d*multipliers.pop())
        
        return ''.join(decoded)
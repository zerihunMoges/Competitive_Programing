class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        for i in range(len(s)):
            
            if s[i] == '(':
                stack.append(i)
                
            elif s[i] == ')':
                if stack:
                    stack.pop()
                    
                elif stars:
                    stars.pop()
                else:
                    return False
                
            else:
                stars.append(i)
        while stack and stars and stars[-1] > stack[-1]:
            stack.pop()
            stars.pop()
            
        return True if stack == [] else False
class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        position = []
        i =0
        leng = len(s)
        while i < leng:
            if s[i] == '(':
                position.append(i)
                i+=1
            elif s[i] == ')': 
                s[position[-1]+1:i] = s[position[-1]+1:i][::-1]
                s.pop(i)
                s.pop(position.pop())
                i-=1
                leng -= 2
            else:
                i += 1

        return ''.join(s)

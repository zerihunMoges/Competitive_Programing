class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ex = {}
        visited = set()
        
        for i in s:
            if i not in ex:
                ex[i] = 1
            else:
                ex[i] += 1

        ans = []
        for i in range(len(s)):
            while ans and ord(ans[-1]) >= ord(s[i]) and ex[ans[-1]] > 1 and s[i] not in visited:     
                du = ans.pop()
                ex[du] -= 1
                visited.remove(du)

            if s[i] not in visited:
                ans.append(s[i])
                visited.add(s[i])
            else:
                ex[s[i]] -= 1
                
        return "".join(ans)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        stack = []
        count = []
        
        for i in range(len(s)):
            count.append(1 if not count or stack[-1] != s[i] else count[-1]+1)
            stack.append(s[i])
            
            if count[-1] >= k:
                for j in range(k):
                    stack.pop()
                    count.pop()
                    
        return ''.join(stack)
            
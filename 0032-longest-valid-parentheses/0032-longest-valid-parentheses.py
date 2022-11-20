class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest = 0
        lastvalid = None
        opening = '('
        closing = ')'
        for i in range(len(s)):
        
            if s[i] == opening:
                stack.append(i)
                
            elif stack:
                removed = stack.pop()
                if lastvalid == None or removed < lastvalid:
                    lastvalid = removed
                    
                if not stack:
                    cur_valid = lastvalid
                    
                else:
                    cur_valid = stack[-1]+1
                    
                longest = max(longest, i-cur_valid + 1)
                
            else:
                lastvalid = None
                
        return longest
        
        
                
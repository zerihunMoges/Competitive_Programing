class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        
        
        def generate(b=[], left=0, right=0):
        
            if right == n:
                ans.append(''.join(b))
                return 
            
            if right < left:
                b.append(')')
                generate(b, left, right+1)
                b.pop()
            if left < n:
                b.append('(')
                generate(b, left+1, right)
                b.pop()
            
            
        generate()
        
        return [ ''.join(ans[i]) for i in range(len(ans))]
            
            
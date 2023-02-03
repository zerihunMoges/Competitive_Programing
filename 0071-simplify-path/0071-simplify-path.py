class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        s = []
        for i in path:

            if i and i != '..' and i!= '.':
                s.append('/'+i)
            if s and i == '..':
                s.pop()
        
        return ''.join(s) if s else '/'
        
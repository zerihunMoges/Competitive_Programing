class Solution:
    def isValid(self, s):
        if len(s)>1 and s[0] == '0':
            return False
        
        return 0 <= int(s) <= 255
    
    def ip(self, s, dots):
        if dots == 3:
            if self.isValid(s):
                return [[s]]
            return []
        
        possible = []
        for i in range(1,min(4,len(s))):
            if self.isValid(s[:i]):
                result = self.ip(s[i:], dots+1)
                for r in result:
                    possible.append([s[:i]]+r)
                
        return possible
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = self.ip(s, 0)
        return [ '.'.join(a) for a in ans]        
        
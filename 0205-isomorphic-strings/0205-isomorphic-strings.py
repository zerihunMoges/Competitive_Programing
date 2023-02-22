class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappedto = {}
        mappedfrom = {}
        for i in range(len(s)):
        
           
            if s[i] in mappedfrom and mappedfrom[s[i]] != t[i]:
                return False
            
            if t[i] in mappedto and mappedto[t[i]] != s[i]:
                return False
            
            
            mappedto[t[i]] = s[i]
            mappedfrom[s[i]] = t[i]
        
        return True
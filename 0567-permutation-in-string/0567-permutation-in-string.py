class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        c = Counter(list(s1))
        
        window = sum(c.values())
        v = Counter(s2[:window-1])
        for i in range(window-1, len(s2)):
            v[s2[i]] += 1
            if v == c:
                return True
            
            v[s2[i-window+1]] -= 1
            
        return False
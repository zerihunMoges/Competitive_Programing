class Solution:
    def interleave(self, s1idx, s1, s2idx, s2, s3, memo):
        
        if (s1idx, s2idx) in memo:
            return False
        
        if s1idx >= len(s1) and s2idx >= len(s2) and s1idx+s2idx >= len(s3):
            return True
        
        if s1idx+s2idx >= len(s3):
            return False
        
        if s1idx < len(s1) and s1[s1idx] == s3[s1idx+s2idx] and self.interleave(s1idx+1,s1, s2idx,s2, s3, memo):
            return True
        if s2idx < len(s2) and s2[s2idx] == s3[s1idx+s2idx] and self.interleave(s1idx,s1, s2idx + 1,s2, s3, memo):
            return True
        
        memo.add((s1idx, s2idx))
        return False
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = set()
        return self.interleave(0, s1, 0, s2, s3, memo)
        
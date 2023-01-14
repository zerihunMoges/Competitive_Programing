class Solution:
    def find(self, cur, root):
        if root[ord(cur)-ord('a')] == cur:
            return cur
        
        root[ord(cur)-ord('a')] = self.find(root[ord(cur)-ord('a')], root)
        return root[ord(cur)-ord('a')]
    
    def union(self, l1, l2, root):
        f_root = self.find(l1, root)
        s_root = self.find(l2, root)
            
        if f_root > s_root:
            root[ord(f_root)-ord('a')] = s_root
        else:
            root[ord(s_root)-ord('a')] = f_root
            
            
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        
        root = [chr(i+ord('a')) for i in range(26)]
        for i in range(len(s1)):
            
            first = s1[i]
            second = s2[i]
            self.union(first, second, root)
            
        answer = []
            
        for l in baseStr:
            answer.append(self.find(l, root))
            
        return ''.join(answer)
            
 
        
        
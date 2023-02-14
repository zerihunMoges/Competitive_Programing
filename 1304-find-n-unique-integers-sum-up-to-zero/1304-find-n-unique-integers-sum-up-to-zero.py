class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        ini = [ i for i in range(1, n)]
        ini.append(-sum(ini))
        return ini
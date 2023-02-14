class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))
        
        for i in range(32):
            if Counter(str(1 << i)) == count:
                return True
        return False
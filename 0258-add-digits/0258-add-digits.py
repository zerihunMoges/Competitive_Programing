class Solution:
    def addDigits(self, num: int) -> int:
        
        
        n = sum(list(map(int, list(str(num)))))
        m = sum(list(map(int, list(str(n)))))
        return  sum(list(map(int, list(str(m)))))
class Solution:
    def cross(self, prev, num, stones, end, memo):
        if num == end:
            return True
        
        if num not in stones or (prev, num) in memo:
            return False
        
        
        for i in range(prev-1, prev+2):
            if i > 0 and self.cross(i, num+i, stones, end, memo):
                return True
        
        memo.add((prev, num))
        
        return False
        
    def canCross(self, stones: List[int]) -> bool:
        
        start = stones[0]
        end = stones[-1]
        memo = set()
        stones = set(stones)
        prev = 0
  
        return self.cross(prev,start, stones, end, memo)
    
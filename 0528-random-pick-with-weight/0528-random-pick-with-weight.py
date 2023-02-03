class Solution:

    def __init__(self, w: List[int]):
        self.pre = w
        self.tot = sum(w)
        for i in range(1, len(self.pre)):
            self.pre[i] += self.pre[i-1]
        
    def binary(self, rand):
        left = 0
        right = len(self.pre)-1
        best = 0
        while left <= right:
            mid = (left+right)//2
            
            if rand <= self.pre[mid]:
                right = mid - 1
                best = mid
            else:
                left = mid + 1
                
        return best
    
    def pickIndex(self) -> int:
        rand = random.randint(1, self.tot)
        return self.binary(rand)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
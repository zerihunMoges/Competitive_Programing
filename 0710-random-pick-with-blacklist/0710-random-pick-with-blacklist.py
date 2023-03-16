class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        bl = sorted(blacklist)
        self.blacklist = set(blacklist)
        self.n = n
     
        self.free = n - len(blacklist)
        self.map = defaultdict(int)
        j = 0
        for i in range(self.free, n):
            if i not in self.blacklist:
                self.map[bl[j]] = i
                
                j+=1

    def pick(self) -> int:
        picked = None
    
        picked = random.randint(0, self.free-1)
            
        return self.map[picked] if picked in self.map else picked

    
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
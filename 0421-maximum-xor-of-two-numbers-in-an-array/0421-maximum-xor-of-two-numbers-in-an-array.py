class Solution:
    def insert(self, trie, num):
        current = trie
        for i in range(30,-1, -1):
            
            if num& (1<<i) in current:
                current = current[num& (1<<i)]
            else:
                current[(num& (1<<i))] = {}
                current = current[num& (1<<i)]
                
    def findBest(self, trie, num):      
        current = trie
        best = 0
        for i in range(30,-1, -1):
            # print(num, (num & (1 << i))^1)
            if (num & (1 << i))^(1 << i) in current:
                current = current[(num & (1 << i))^(1 << i)]
                best += 1 << i
           
            else:
                current = current[(num & (1 << i))]
                
        return best
                
    def findMaximumXOR(self, nums: List[int]) -> int:
      
        trie = {}
        for num in nums:
            self.insert(trie, num)
            
        
        best = 0
        for num in nums:
            best = max(self.findBest(trie, num), best)
            
        return best
        

        
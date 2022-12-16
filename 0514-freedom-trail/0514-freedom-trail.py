class Solution:
    
    def findMinSteps(self, k, r, memo, ring, key, direction):
        
        if k >= len(key):
            return 0
        
        if (k,r,direction) in memo:
            return memo[(k,r,direction)]
        
        left = float('inf')
        right = float('inf')
        look = float('inf')
        
        if key[k] == ring[r]:
            left = 1+self.findMinSteps(k+1,r,memo, ring, key, -1)
            right = 1+self.findMinSteps(k+1,r,memo, ring, key, 1)
            
        else:
            look = 1+ self.findMinSteps(k, (len(ring) + r+direction)%len(ring), memo, ring, key, direction)
            
        memo[(k,r,direction)] = min(left, right, look)
        
        return memo[(k,r,direction)]
            
            
            
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = defaultdict(int)
        
        return min(self.findMinSteps(0,0,memo, ring, key, 1), self.findMinSteps(0,0,memo, ring, key, -1))
        
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]],i=0, b = defaultdict(int)) -> int:

        if i >= len(requests):
            
            if all([b[key] == 0 for key in b]) :
                return 0
            else:
                return -float('inf')
            
            
        fbuild, tobuild = requests[i]
        b[fbuild]-=1
        b[tobuild]+=1
        take = 1+self.maximumRequests( n, requests,i+1, b)
        b[fbuild]+=1
        b[tobuild]-=1
        
        skip = self.maximumRequests(n ,requests,i+1, b)
        
        
        return max(take, skip)
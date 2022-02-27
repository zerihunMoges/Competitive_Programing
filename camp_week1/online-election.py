class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leaderboard = []
        self.times = times
        votecount = [0]*len(persons)
        top = 0
        
        for i in range(len(persons)):
            
            votecount[persons[i]] += 1
            if votecount[persons[i]] >= votecount[top]:
                top = persons[i]
                
            self.leaderboard.append(top)
       

    def q(self, t: int) -> int:
        left= 0
        right=len(self.times)-1
        extime = None
        while left<=right:
            mid = (left+right)//2
            
            if self.times[mid] > t:
                right = mid-1
                
            elif self.times[mid] < t:
                left = mid+1
            else:
                extime = mid
                break
                
        if extime == None:
            extime = left-1
                
        return self.leaderboard[extime]
                

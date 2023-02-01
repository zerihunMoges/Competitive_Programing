class Solution:
    def bestTeam(self,i , min_i, scores, memo):
        if i >= len(scores):
            return 0
        
        if (i, min_i) in memo:
            return memo[(i, min_i)]
        
        pick = 0
        skip = 0
        
        if scores[i][0] >= scores[min_i][0]:
            pick = scores[i][0] + self.bestTeam(i+1, i , scores, memo)
            
        skip = self.bestTeam(i+1, min_i, scores, memo)
        memo[(i, min_i)] = max(pick, skip)
        return memo[(i, min_i)]
        
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        some = [[scores[i], ages[i]] for i in range(len(scores))]
        some.sort(key = lambda x: [x[1], x[0]])
        memo = defaultdict(int)
            
        for i in range(len(some)):
            for j in range(i):
                if some[i][0] >= some[j][0]:
                    memo[i] = max(memo[i], memo[j])
                    
            memo[i] += some[i][0]
        
        
        return max(memo.values())
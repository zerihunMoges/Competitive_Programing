class Solution:
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
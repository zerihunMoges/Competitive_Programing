class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        di = defaultdict(int)

        for i in candidates:
            cur = list(reversed(bin(i)[2:]))
            
            for j in range(len(cur)):
                if cur[j] == '1':
                    di[j] += 1
        return max(di.values())

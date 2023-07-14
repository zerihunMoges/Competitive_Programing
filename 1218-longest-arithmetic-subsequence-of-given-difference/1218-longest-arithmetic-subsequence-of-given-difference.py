class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        seq = defaultdict(int)
        left = 0
        for i in range(len(arr)):
            if arr[i] - difference in seq:
                seq[arr[i]] = max(seq[arr[i]], seq[arr[i]-difference]+1)
            else:
                seq[arr[i]] = 1
                
        return max(seq.values())
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        score = 0
        
        @lru_cache()
        def play(i,j, turn):
            nonlocal score
           
            
            if i > j :
                return 0
               
            if turn == 0:
                result = max(nums[i] + play(i+1, j, 1), nums[j] + play(i, j-1, 1))
                return result
            else:
                result = min(play(i , j -1, 0), play(i+1, j, 0))
                return result
            
        score = play(0, len(nums)-1, 0)

        return score >= sum(nums) - score
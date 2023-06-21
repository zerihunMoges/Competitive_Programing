class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        my = sorted([[nums[i],cost[i]] for i in range(len(nums))])
        leftcost = [0]*(len(nums))
        rightcost = [0]*(len(nums))
        right_cost_sum = my[-1][1]
        left_cost_sum = my[0][1]
        for i in range(1, len(nums)):
            leftcost[i] = (my[i][0]-my[i-1][0])*left_cost_sum + leftcost[i-1]
            rightcost[-i-1] = abs(my[-i-1][0]-my[-i][0])*right_cost_sum + rightcost[-i]
        
            left_cost_sum += my[i][1]
            right_cost_sum += my[-i-1][1]
       
        best = float('inf')
        for i in range(len(nums)):
            
            best = min(best, leftcost[i]+rightcost[i])
            
        return best
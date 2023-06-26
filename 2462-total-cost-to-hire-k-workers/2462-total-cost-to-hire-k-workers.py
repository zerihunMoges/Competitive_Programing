class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = []
        right = []
        costs = deque(costs)
        total  = 0
        while k > 0:
            
            while len(left) < candidates and costs:
                heapq.heappush(left, costs.popleft())
            while len(right) < candidates and costs:
                heapq.heappush(right, costs.pop())
                
            if left == [] or (right != [] and left[0] > right[0]):
                total += heapq.heappop(right)
            else:
                total += heapq.heappop(left)
            
            k-=1
            
        return total
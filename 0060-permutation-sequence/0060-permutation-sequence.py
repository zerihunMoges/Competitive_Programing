class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:
        
        available = set([i for i in range(1, n+1)])
        answer = ''
        prev = 0
        for j in reversed(range(n)):
            cur = math.factorial(j)+prev
            nums = sorted(available)
            i = 0
            while cur < k:

                cur += math.factorial(j)
                i += 1

            available.remove(nums[i])
            
            answer += str(nums[i])
            prev = cur-math.factorial(j)
        
        return answer
        
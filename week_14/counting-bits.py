class Solution:
    def countBits(self, n: int) -> List[int]:
    
        ans = []
        st = 0
        for i in range(n+1):

            cur = i
            temp = 0
            while cur:
                temp += cur&1
                cur >>= 1
                
            ans.append(temp)
        return ans

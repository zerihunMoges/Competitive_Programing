class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        right = sum(weights)
        left = max(weights)

        bw = right
        while left <= right:
            mid= (left + right)//2
            tempmid = mid
            i=0
            day = days

            while i < len(weights) and day > 0:

                while i < len(weights) and tempmid - weights[i] >=0:
                    tempmid -= weights[i] 
                    i+=1
                day -= 1
                tempmid = mid


            if i == len(weights):
          
                bw = min(mid, bw)
                right = mid-1

            else:
                left = mid+1
                
        return bw

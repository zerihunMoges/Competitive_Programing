class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        missing = 0
        
        prev = 0
        for i in range(len(arr)):
            

            
            if missing + arr[i] - prev - 1 >= k:
                return prev + k-missing
            missing += (arr[i] - prev)-1
            prev = arr[i]

        return prev + k-missing
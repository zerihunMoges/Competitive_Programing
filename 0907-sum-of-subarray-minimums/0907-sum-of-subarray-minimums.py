class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
       
        left_range = defaultdict(lambda: -1)
        right_range = defaultdict(lambda: len(arr))
        next_less = []
        for i in range(len(arr)):
            while next_less and arr[next_less[-1]] > arr[i]:
                removed = next_less.pop()
                right_range[removed] = i

            if next_less:
                left_range[i] = next_less[-1]

            next_less.append(i)

        subarray_min_sum = 0
      
    
        
        for i in range(len(arr)):
            left_len = i - left_range[i]
            right_len = right_range[i] - i
            
            subarray_count = left_len*right_len
            
            subarray_min_sum += arr[i]*subarray_count

        return subarray_min_sum%(10**9+7)
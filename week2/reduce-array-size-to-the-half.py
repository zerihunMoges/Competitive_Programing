class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arry = [0]
        numofset = 0
        sums = 0
        for i in range(len(arr)):
            if len(arry) < (arr[i] +1):
                arry += [0]*(arr[i]-len(arry)+1)
            arry[arr[i]] += 1
            
        arry.sort()
        j=-1
        while sums < len(arr)//2:
            sums += arry[j]
            numofset += 1
            j-=1
        return numofset
        

class Solution: 
    def select(self, arr, i):
        selected = arr[i]
        pos = i
        while i < len(arr):
                if arr[i] <= selected:
                        selected = arr[i]
                        pos = i
                i+=1
        return selected, pos
    
    def selectionSort(self, arr,n):
        i = 0
        for j in range(n):
            selected = self.select(arr,i)
            arr[j],arr[selected[1]]  = selected[0],arr[j]
            i+=1

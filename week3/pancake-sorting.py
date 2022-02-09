class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flip = []
        target = len(arr)
        for i in range(len(arr)):
            j = arr.index(target) + 1
            if target != j:
                if j != 1:
                    flip.append(j)
                    newarry = arr[:j]
                    newarry.reverse()
                    arr = newarry+arr[j:]
                    
                flip.append(target)
                newarry = arr[:target]
                newarry.reverse()
                arr = newarry + arr[target:]
                target -=1
                
            else:
                target -=1
        return flip

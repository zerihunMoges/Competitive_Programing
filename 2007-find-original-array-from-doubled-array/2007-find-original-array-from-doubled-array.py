class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        leng = len(changed)//2
        changed.sort()
        i = 0
        j = 1
        while len(changed) > leng:
            if j >= len(changed):
                return []
            elif changed[i]*2 == changed[j] and i != j: 
                changed.pop(j)
                i+=1
            else:
                j+=1
        original = changed if len(changed) == leng else []
        return original
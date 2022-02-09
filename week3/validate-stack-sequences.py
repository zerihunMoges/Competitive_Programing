class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j= 0
        k=0

        while (j < len(pushed) and k < len(popped)):
            if pushed[j] == popped[k]:
                pushed.pop(j)
                j-=1 if j>0 else 0
                k+=1
            else:
                j+=1

        return pushed==[]

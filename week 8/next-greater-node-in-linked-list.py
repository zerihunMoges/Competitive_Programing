# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        val = []
        j=0
        while head:
            answer.append(0)
            j=2
            while val and val[-1] < head.val:
                if answer[len(answer)-j] != 0:
                    j+=1
                    continue
                answer[len(answer)-j] = head.val
                val.pop()
                j+=1
            val.append(head.val)
            head = head.next
            
        return answer
        return answer

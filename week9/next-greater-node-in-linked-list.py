# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        mono = []
        answer = []
        
        while head:
            answer.append(0)
            while mono and mono[-1][0] < head.val:
                r = mono.pop()
                answer[r[1]] = head.val
                
            mono.append([head.val,len(answer)-1])
            head = head.next
        return answer

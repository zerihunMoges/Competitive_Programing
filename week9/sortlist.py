# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
        lis.sort()
        
        head = ListNode('')
        answer = head
        for i in range(len(lis)):
            head.val = lis[i]
            if i != len(lis)-1:
                head.next = ListNode('')
            head = head.next
            
        return answer

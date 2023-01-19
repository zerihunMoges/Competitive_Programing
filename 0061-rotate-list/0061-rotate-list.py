# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        length = 0
        node = head
        last = None
        while node:
            length += 1
            last = node
            node = node.next
            
        k = k%length
        target = length-k
        newHead = None
        node = head
        for i in range(target-1):
            node = node.next
            
        if node.next:
            newHead = node.next
            node.next = None
            last.next = head
        else:
            newHead = head
            
        return newHead
        
            
            
            
        
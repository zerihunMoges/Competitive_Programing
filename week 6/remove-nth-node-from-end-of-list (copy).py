# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        wanted = head
        current = 0
        prev = head
        node = head.next
        
        while node != None:
            current += 1
            if current >= n:
                prev = wanted
                wanted = wanted.next
            node = node.next
            
            
        if wanted == head:
            return wanted.next
        else:
            prev.next = wanted.next
            
            
        return head 
            

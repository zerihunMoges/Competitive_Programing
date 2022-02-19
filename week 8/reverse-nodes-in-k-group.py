# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, k):
        prev = None
        node = head
        length = k
        nxt = None
        while length > 0:
            if length == k:
                tail = node
            nxt = node.next
            node.next = prev
            
            prev = node
            length -= 1
            if length== 0:
                return prev, nxt, tail
            elif nxt == None:
                return head, None, tail
            node = nxt
            
        
    
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
            
        result = self.reverse(head,k)
        node = result[0] 
        nxt = result[1] 
        tail=result[2]
        length -= k
        while nxt:
            if length < k:
                tail.next = nxt
                break
            result = self.reverse(nxt,k)
            tail.next = result[0]
            nxt = result[1] 
            tail=result[2]
            length -= k
            
        return node
        

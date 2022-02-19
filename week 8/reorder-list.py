# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = head
        current = 0
        middle = head
        while l.next != None:
            l = l.next
            current += 1
            if current%2 == 1:
                middle = middle.next
        
        
        prev = None
        l = middle
        while l:
            nxt = l.next
            l.next = prev
            prev = l
            
            l = nxt
        
        
        l = head
        while l.next and prev.next:
            nxt =l.next
            
            l.next = prev
            
            prevnxt = prev.next
            l.next.next = nxt
            
            prev = prevnxt
            l = l.next.next
            

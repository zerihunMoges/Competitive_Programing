# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        even_head = None
        even = None
        odd = head
        
        
       
        if odd:
            even = head.next
            even_head = even
            
        while odd:
            if odd.next:
                odd.next = odd.next.next
            
            if even and even.next:
                even.next = even.next.next
            
            if not odd.next:
                odd.next = even_head
                return head
            
            odd = odd.next
            even = even.next
            
        print(head, even_head)
        
        
        
            
            
            

            
        
    
        
        
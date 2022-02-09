# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slist = head
        
        head = slist
        
        while slist != None:
            if slist.next and slist.val == slist.next.val:
                slist.next = slist.next.next
            else:
                slist = slist.next
        
                
        return head

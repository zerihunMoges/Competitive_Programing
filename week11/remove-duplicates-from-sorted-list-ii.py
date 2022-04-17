# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        start = ListNode('')
        ans =start
        du = None
        while head:
            if head.next and head.val == head.next.val:
                du = head.val
    
            else:
                du = None
                if start.val != '':
                    start.next = ListNode('')
                    start = start.next
                
            while head and head.val == du:
                head = head.next
            
            if du == None:
                start.val = head.val
                head = head.next
                
        return ans

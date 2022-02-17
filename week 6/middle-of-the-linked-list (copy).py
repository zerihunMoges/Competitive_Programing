# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        current = 0
        middle = head
        while l.next != None:
            l = l.next
            current += 1
            if current%2 == 1:
                middle = middle.next
            
                
                
        return middle
            

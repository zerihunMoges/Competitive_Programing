# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        first = head
        
        second = head.next if head else None
        
        while first and second:
            if first == second:
                return True
            first = first.next
            second = second.next.next if second and second.next else None
             
        return False

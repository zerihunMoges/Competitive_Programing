# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
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
        
        
        while prev and head:
            
            if prev.val != head.val:
                return False
            
            prev = prev.next
            head = head.next
        return True

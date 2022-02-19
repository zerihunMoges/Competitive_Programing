# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = head
        current = 0
        middle = head
        while l.next != None:
            l = l.next
            current += 1
            if current%2 == 1:
                middle = middle.next
        
        #reverse second half
        prev = None
        l = middle
        while l:
            nxt = l.next
            l.next = prev
            prev = l
            
            l = nxt
        
        maxsum = 0  
        while prev:
            result = prev.val + head.val
            if result > maxsum:
                maxsum = result
            prev = prev.next
            head = head.next
        
        return maxsum

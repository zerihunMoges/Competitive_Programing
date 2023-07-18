# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        def findValue(l1):
            num = 0
            while l1:
                num += l1.val
                if l1.next:
                    num *= 10
                l1 = l1.next
                
            return num
        
        
        tot = str(findValue(l1) + findValue(l2))

        newHead = ListNode()
        cur = newHead
        for i in range(len(tot)):
            cur.val = int(tot[i])
            
            if i < len(tot)-1:
                cur.next = ListNode()
            cur = cur.next
            
        return newHead
            
            
            
        
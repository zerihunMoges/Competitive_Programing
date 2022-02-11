
        #Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            
            
            nxt = head.next
            nxtnxt = nxt.next
            nxt.next = head
            
            head.next = self.swapPairs(nxtnxt)
            return nxt
       

    #Loop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = head
        if head and head.next:
            nodes = head.next
        prev = ListNode()
        while head and head.next:
            
            m = head.next.next
            pre = head
            cur = head.next
            head = cur
            cur.next = pre
            pre.next = m
            
            head = m
            prev.next = cur
            prev = pre
        
            
            
        return nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortd = ListNode(-float("inf"))
        start = sortd
        cur = head
        print([random.randint(-5000, 5000) for i in range(199)])
        while cur:
            start = sortd
            prev = None
            while start and cur.val > start.val:
                prev = start
                start = start.next
            
            print(cur.val)
            if prev:   
                prev.next = ListNode(cur.val)
                prev.next.next = start
            else:
                nex = sortd.next
                print(sortd)
                sortd.next = ListNode(cur.val)
                sortd.next.next = nex
                
            cur = cur.next
            
        return sortd.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val
    def __gt__(self, other):
        return self.val > other.val
    
    
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i in lists:
            if i:
                heapq.heappush(heap, ListNode(i.val, i.next))
      
        merged = ListNode('')
        head = merged
        
        
        while heap:
            
            minn = heapq.heappop(heap)
            merged.val = minn.val
            if minn.next:
                minn = minn.next
                heapq.heappush(heap, ListNode(minn.val, minn.next))
            
            if heap:
                merged.next = ListNode('')
                merged = merged.next
                
        
        return head
            
            
            
            

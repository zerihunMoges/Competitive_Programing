"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flat(self, head):
        if head == None or (head.next == None and head.child == None):
            return head
        
        temp = head.next
        child_tail = self.flat(head.child)
        
        if child_tail:
            head.next = head.child
            child_tail.next = temp
            if head.next:
                head.next.prev = head
            if temp:
                temp.prev = child_tail
            
            
        q_tail = self.flat(temp)
        head.child = None
        return q_tail if q_tail else child_tail
    
    
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tail = self.flat(head)
        
        return head
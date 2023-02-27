"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyR(self, head, new):
        if not head:
            return head
        
        newHead = new[head] 
        
        if newHead == None:
            newHead = Node(head.val)
            
        new[head] = newHead
        
        if head.next != None and head.next in new:
            newHead.next = new[head.next]
            
        else:
            nxt = self.copyR(head.next, new)
            new[head.next] = nxt
            newHead.next = nxt
            
        if new[head.random] != None:
            newHead.random = new[head.random]
            
        else:
            rand = self.copyR(head.random, new)
            new[head.random] = rand
            newHead.random = rand
            
        return newHead
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        return self.copyR(head, defaultdict(lambda: None))
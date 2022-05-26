class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
     

    def get(self, index: int) -> int:
        start = self.head
        
        if start:
            for i in range(index):

                start = start.next
                if start == None:
                    return -1
                  
            return start.value
        return -1
    
    def addAtHead(self, val: int) -> None:
        head = self.head
        
        newnode = Node(val)
        newnode.next = head
        self.head = newnode
        
        
    def addAtTail(self, val: int) -> None:
        head = self.head
        while head and head.next:
            head = head.next
        newnode = Node(val)    
        if head:
            head.next = newnode
        else:
            self.head = newnode

    def addAtIndex(self, index: int, val: int) -> None:
        head = self.head
        newnode = Node(val) 
        
        for i in range(index-1):

            head = head.next if head else None
            if head == None:
                return 


        if index > 0:
            if head:
                nxt = head.next 
                head.next = newnode
                newnode.next = nxt
                return
        
        else:
            newnode.next = head
            self.head = newnode

    def deleteAtIndex(self, index: int) -> None:
        head = self.head
        
        if head:
            for i in range(index-1):
                head = head.next
                if head == None:
                    return 
        
            if index > 0:
                nxt = head.next
                head.next = nxt.next if nxt else None
            else:
                self.head = head.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class ListNode:
    def __init__(self, key, val, prv=None, nxt=None):
        self.key = key
        self.val = val
        self.prv = prv
        self.nxt = nxt
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.nodes = defaultdict()
        self.stack = []
                                 
                
    def remove(self, key):
        if key == 7:
            print('removed: ', key)
        if key not in self.nodes:
            return 
        node = self.nodes[key]
        prv = node.prv
        nxt = node.nxt
        
        if prv and nxt:
            prv.nxt = nxt
            nxt.prv = prv
        if not prv:
            self.head = nxt
            if nxt:
                nxt.prv = None
        if not nxt:
            self.tail = prv
            if prv:
                prv.nxt = None
        
        del self.nodes[key]
    def add(self, key, val):
        if key == 7:
            print('added: ', key)
        node = ListNode(key, val)
        node.nxt = self.head
        if self.head:
            self.head.prv = node
        if not self.tail:
            self.tail = node
    
        
        self.head = node
        self.nodes[key] = node
        
    def removeLast(self):
        
        if self.tail:
            deleted = self.tail
            prv = self.tail.prv
            self.tail = prv
            if prv:
                prv.nxt = None
            else:
                self.head = None
                
            del self.nodes[deleted.key]
            
    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.remove(key)
            self.add(key, node.val)
            return self.nodes[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(key)        
        self.add(key,value)
        if len(self.nodes) > self.capacity:
            self.removeLast()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class DLinkedList:
    def __init__(self,key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.lrucache = {}
        self.capacity = capacity
        self.lrufirst = None
        self.lrulast = None
   
    def get(self, key: int) -> int:
        if key not in self.lrucache:
            return -1
        
        if self.lrucache[key].left:
            self.lrucache[key].left.right = self.lrucache[key].right
        if self.lrucache[key].right:
            self.lrucache[key].right.left = self.lrucache[key].left
        
        self.lrucache[key].left = self.lrulast
        self.lrucache[key].right = None
        
        return self.lrucache[key].val

    def put(self, key: int, value: int) -> None:
        print(key)
        if key not in self.lrucache and self.capacity == len(self.lrucache):
            print('got')
            self.lrucache.pop(self.lrufirst.key)
            print(self.lrufirst.key)

            self.lrufirst = self.lrufirst.right
            print(self.lrufirst.key)
            
        if key not in self.lrucache:
            self.lrucache[key] = DLinkedList(key, value)
            self.lrucache[key].left = None
            self.lrucache[key].right = None
            if self.lrufirst:
                self.lrulast.right = self.lrucache[key]
                self.lrucache[key].left = self.lrulast
                self.lrulast = self.lrulast.right
                

            else:
                self.lrufirst = self.lrucache[key]
                self.lrulast = self.lrucache[key]
                
        elif key in self.lrucache:
            right = self.lrucache[key].right
            left = self.lrucache[key].left
            left.right = right
            right.left = left

            self.lrucache[key].left =right
            self.lrucache[key].right = None
            self.lrucache[key].val = value

class MajorityChecker:

    def __init__(self, arr: List[int]):
        
        self.arr = arr
        self.indexes = defaultdict(list)
        for i in range(len(arr)):
            self.indexes[arr[i]].append(i)
            
    def findRight(self, target, arr):
        left = 0 
        right = len(arr)-1
        l = None
        while left <= right:
            mid = (left+right)//2
            
            if arr[mid] < target:
                left = mid+1
                
                
            elif arr[mid] >= target:
                right = mid-1
                l = mid
                
        return l
    
    def findLeft(self,target, arr ):
        
        left = 0 
        right = len(arr)-1
        l = None
        while left <= right:
            mid = (left+right)//2
            
            if arr[mid] <= target:
                left = mid+1
                l = mid
                
            elif arr[mid] > target:
                right = mid-1
                
        return l
    def query(self, left: int, right: int, threshold: int) -> int:
        for i in range(10):
            target = self.arr[random.randint(left, right)]
            start = self.findRight(left, self.indexes[target])
            end = self.findLeft(right, self.indexes[target])
            
            if end-start +1 >= threshold:
                return target
            
        return -1
        

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

count
112211
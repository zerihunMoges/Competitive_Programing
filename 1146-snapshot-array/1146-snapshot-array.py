class SnapshotArray:

    def __init__(self, length: int):
        
        self.e = defaultdict(lambda: [[0, 0]])
        self.cur_snap = 0
    def set(self, index: int, val: int) -> None:
        self.e[index].append([self.cur_snap, val])
        
        

    def snap(self) -> int:
        self.cur_snap += 1
        return self.cur_snap - 1
    def get(self, index: int, snap_id: int) -> int:
        
        left = 0
        right = len(self.e[index])-1
        best = 0
        while left <= right:
            mid = (left+right)//2
            if self.e[index][mid][0] > snap_id:
                right = mid-1
                
            else:
                best = mid
                left = mid+1
        return self.e[index][best][1]
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        bb = -1
        while left <= right:
            mid = (left+right)//2
            if isBadVersion(mid):
                bb = mid
                right = mid-1
            else:
                left = mid+1
                
        return bb

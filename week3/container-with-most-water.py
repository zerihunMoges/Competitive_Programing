class Solution:
    def maxArea(self, height: List[int]) -> int:
        j= 0
        k=len(height)-1
        maxarea = 0
        for i in range(len(height)):
            maxarea = max(maxarea, min(height[j], height[k])*(k-j))
            if height[j] >= height[k]:
                k-=1
            elif height[k] > height[j]:
                j += 1

        return maxarea

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        time = float("inf")
        prev = None
        for i in range(len(timePoints)+1):
            t = list(map(int, timePoints[i%len(timePoints)].split(":")))
            cur = t[0]*60+t[1]
            if prev != None:
                time = min(cur - prev if cur - prev >= 0 else cur - prev + 24*60 , time)
            prev = cur
        return time
            

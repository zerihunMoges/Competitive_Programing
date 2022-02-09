class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = 0
        end = 0
        i = 0
        while i < (len(intervals)-1):
            start = intervals[i][0]
            end = intervals[i][1]
            if  end >= intervals[i+1][1]:
                intervals[i] = [start, end]
                intervals.pop(i+1)
            elif end >= intervals[i+1][0]:
                intervals[i] = [start, intervals[i+1][1]]
                intervals.pop(i+1)
            else:
                i+=1
            
        return intervals

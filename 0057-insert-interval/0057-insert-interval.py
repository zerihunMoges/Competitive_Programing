class Solution:
    
    def overlap(self, f_start, f_end, s_start, s_end):
        
        return min(f_end, s_end) >= max(s_start, f_start)
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        answer = []
        for i in range(len(intervals)):
            
            if newInterval:
                if answer and self.overlap(newInterval[0], newInterval[1], answer[-1][0], answer[-1][1]):
                    answer[-1][0] = min(newInterval[0], answer[-1][0])
                    answer[-1][1] = max(newInterval[1], answer[-1][1])
                    newInterval = None
                elif newInterval[0] <= intervals[i][0] or self.overlap(newInterval[0], newInterval[1], intervals[i][0], intervals[i][1]):
                    answer.append(newInterval)
                    newInterval = None
                    
            if answer and self.overlap(intervals[i][0], intervals[i][1], answer[-1][0], answer[-1][1]):
                answer[-1][0] = min(intervals[i][0], answer[-1][0])
                answer[-1][1] = max(intervals[i][1], answer[-1][1])
            else:
                answer.append(intervals[i])
                
        if newInterval:
            answer.append(newInterval)
            
        return answer
                
                    
                
                
            
                

                
                
                
                
                
                
    
    
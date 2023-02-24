class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        
        answer = [0]*k
        
        
        uam = defaultdict(set)
        
        for idi, time in logs:
            uam[idi].add(time)
            
        for user in uam:
            if len(uam[user]) - 1 < len(answer):
                answer[len(uam[user])-1] += 1
                
        return answer
            
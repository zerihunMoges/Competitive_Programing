class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        skills = []
        for peopleSkill in people:
            skillBits = 0
            for skill in peopleSkill:
                pos = req_skills.index(skill)
                
                skillBits |= 1 << pos
                
            skills.append(skillBits)
        
        @lru_cache(maxsize=None)
        def minSufficientTeam(sk, i):
            if sk == 2**(len(req_skills))-1:
                return 0, []
            if i >= len(people):
                return float('inf'), []
            
            pick, pPicked = minSufficientTeam(sk|skills[i], i+1) 
            skip, sPicked = minSufficientTeam(sk, i+1)
            
            if pick < skip:
                return 1+pick, [i] + pPicked
            return skip, sPicked
        
        return minSufficientTeam(0, 0)[1]
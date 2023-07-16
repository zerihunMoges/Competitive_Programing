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
                return []
            if i >= len(people):
                return None
            
            pick = minSufficientTeam(sk|skills[i], i+1) 
            skip = minSufficientTeam(sk, i+1)
            
            if pick != None and (not skip  or len(pick) < len(skip)):
                return pick + [i]
            return skip
        
        return minSufficientTeam(0, 0)
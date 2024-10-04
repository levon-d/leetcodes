class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2: 
            return skill[0] * skill[1]
            
        if sum(skill) % (len(skill) // 2) != 0:
            return -1

        skill.sort()
        teams = []

        l, r = 0, len(skill)-1 
        result = 0 

        while l<r:
            current_team = (skill[l], skill[r]) 
            if teams and (current_team[0] + current_team[1]) != (teams[-1][0] + teams[-1][1]):
                return -1 
            
            teams.append(current_team)
            result += (current_team[0] * current_team[1])
            l+=1 
            r-=1 
    
        return result
        




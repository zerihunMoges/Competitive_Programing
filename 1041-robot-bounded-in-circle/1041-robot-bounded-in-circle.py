class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        dirc = 0
        
        
        for ins in instructions:
            if ins == 'R':
                dirc = (dirc+1)%len(directions)
            elif ins == 'L':
                dirc = (dirc-1+ len(directions))%len(directions)  
            else:
                pos[0] += directions[dirc][0]
                pos[1] += directions[dirc][1]
                
        if pos == [0,0] or dirc != 0:
            return True
        return False
        
        
        
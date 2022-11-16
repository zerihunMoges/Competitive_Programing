class Solution:
    def racecar(self, target: int) -> int:
        memo = defaultdict(int)
        moves = deque([[0,1, 0]])
        visited = set()
        while moves:
            
            pos, speed, move = moves.popleft()
            if pos == target:
                return move
            
            a_pos, a_speed = pos+speed, speed*2
            r_pos, r_speed = pos, -1*(abs(speed)//speed)
        
            if -target <= a_pos <= 2*target and (a_pos, a_speed) not in visited:
                visited.add((a_pos, a_speed))
                moves.append([a_pos, a_speed, move+1])
                
            if -target/2 <= r_pos <= target + target/2 and (r_pos, r_speed) not in visited:
                visited.add((r_pos, r_speed))
                moves.append([r_pos, r_speed, move+1])
                
        return -1
        
        
        
                
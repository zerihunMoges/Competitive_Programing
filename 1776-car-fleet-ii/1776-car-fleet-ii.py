class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        times = [-1]*len(cars)
        collisions = []          
        for i in reversed(range(len(cars))):
            cur_pos, cur_speed = cars[i]
            
            while collisions:
                pos, speed, time = collisions[-1]
                if cur_speed > speed and ((pos - cur_pos)/(cur_speed - speed) < time or time == -1):
                    times[i] = (pos - cur_pos)/(cur_speed - speed)
                    break 

                else:
                    collisions.pop()
                    
            collisions.append([cur_pos, cur_speed, times[i]])
            
        return times
    

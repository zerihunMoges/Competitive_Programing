class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleets = []
        pos_speed = sorted(zip(position,speed), reverse=True)
        for pos, speed in pos_speed:
            time = (target- pos)/speed
            if car_fleets and time > car_fleets[-1]:
                car_fleets.append(time)
            elif car_fleets == []:
                car_fleets.append(time)
                
        return len(car_fleets)

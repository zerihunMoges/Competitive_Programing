class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        tot = 0
        for i in range(len(seats)):
            tot += abs(seats[i]-students[i])
            
        return tot
            
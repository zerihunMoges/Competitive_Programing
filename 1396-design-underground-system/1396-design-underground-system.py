class UndergroundSystem:

    def __init__(self):
        self.checkin_times = defaultdict(list)
        self.travels = defaultdict(lambda: defaultdict(lambda: defaultdict(int) ))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_times[id] = [t, stationName]
       
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_time, checkin_station = self.checkin_times[id]
        
        self.travels[checkin_station][stationName]['total_time'] += t-checkin_time
        self.travels[checkin_station][stationName]['total_travel']  += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return self.travels[startStation][endStation]['total_time'] / self.travels[startStation][endStation]['total_travel']

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
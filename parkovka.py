'''
from parkovka import Parkovka
parking = Parkovka()
parking.addCar(id)
cost = parking.getCost(id)
parking.removeCar(id, cost)
parking.addBalance(id, balance)
parking.removeCar(id)
parking.history_id(id, start_date, end_date)
parking.history_parking(start_date, end_date)
parking.getCost()
parking.getAverage()
parking.getCarsCount()
parking.getAvailableParkingCount()
'''
import bisect
from collections import defaultdict
from time import time
import datetime

class Parkovka:
    def __init__(self, N, cost):
        self.cost = cost
        self.parked = defaultdict(float)
        self.history = []
        self.balance = defaultdict(int)
        self.car_length = defaultdict(int)
        self.color = defaultdict(str)
        
        self.parkingCount = N
    
    def addBalance(self, id, balance):
        self.balance[id] += balance

    def removeBalance(self, id, balance):
        self.balance[id] -= balance
    
    def setCost(self, cost):
        self.cost = cost
    
    def getCostPerHour(self):
        return self.cost
    
    def addCar(self, id, start=None):
        if start:
            self.parked[id] = self.getTimestamp(start)
        else:
            self.parked[id] = time()
        self.parkingCount -= 1

    def getTotalCost(self, id):
        start = self.parked[id]
        end = time()
        total = int((end - start)/3600 * self.cost)
        return total

    def removeCar(self, id, cost = None):
        if cost == None:
            cost = self.getTotalCost(id)
            self.removeBalance(id, cost)
        self.history.append( (self.parked[id], time(), id, cost))
        del self.parked[id]
        self.parkingCount += 1
    
    def getParkedCount(self):
        return len(self.parked)

    def getAvailableParkingCount(self):
        return self.parkingCount
    
    def getAverage(self):
        arr = [cost for _, _, _, cost in self.history]
        return sum(arr) / len(arr)

    def getTimestamp(self, date_string):
        date_object = datetime.datetime.strptime(date_string, "%d-%m-%Y")
        return int(date_object.timestamp())

    def getHistory_id(self, id, start, end):
        arr = []
        start = self.getTimestamp(start)
        end = self.getTimestamp(end)
        for h_start, h_end, h_id, cost in self.history:
            if id == h_id and not (end < h_start or h_end < start):
                arr.append((h_start, h_end, cost))
        return arr

    def getHistory_parking(self, start, end):
        arr = []
        start = self.getTimestamp(start)
        end = self.getTimestamp(end)
        for h_start, h_end, h_id, cost in self.history:
            if not (end < h_start or h_end < start):
                arr.append( (h_start, h_end, h_id, cost))
        return arr
    

        



    



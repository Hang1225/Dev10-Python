import csv
import random

class astronaut:
    def __init__(self,name,flight,status,gender='',birthplace='',missions=[]):
        self.__name = name
        self.__status = status
        self.__flight = int(flight.strip())
        self.__gender = gender
        self.__birthplace = birthplace
        self.__missions = missions
    
    def __str__(self):
        return f'{self.name}, {self.status}'
        
    def __gt__(self,other):
        print (f'greater than called\nself: {self.flight} | other: {other.flight}')
        return self.flight > other.flight

    def __ge__(self,other):
        print (f'greater than or equal to called\nself: {self.flight} | other: {other.flight}')
        return self.flight >= other.flight

    def __eq__(self,other):
        print (f'equal called\nself: {self.flight} | other: {other.flight}')
        return self.flight == other.flight

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,new):
        self.__name = new
        return
    
    @property 
    def status(self):
        return self.__status

    @status.setter
    def status(self,new):
        self.__status = new
        return

    @property
    def flight(self):
        return self.__flight
    
    @flight.setter
    def flight(self,new):
        self.__flight = new
        return

    @property
    def gender(self):
        return self.__gender

    @property
    def birthplace(self):
        return self.__birthplace

    @property
    def missions(self):
        return self.__missions

def importFiles():
    with open('astronauts.csv','r') as file:
        temp = [{x:y for x,y in x.items()} for x in csv.DictReader(file)]
    return [astronaut(x['Name'],x['Space Flight (hr)'],x['Status'],x['Gender'],x['Birth Place'],x['Missions']) for x in temp]

#list mutable traits of first astronaut
listAstronauts = importFiles()
listAstronauts[0].name = 'John John'
listAstronauts[0].status = 'Retired'
listAstronauts[0].flight = 25

#compare random 2 astronauts
random.seed()
print(listAstronauts[random.randrange(1,len(listAstronauts))] > listAstronauts [random.randrange(1,len(listAstronauts))])
print(listAstronauts[random.randrange(1,len(listAstronauts))] >= listAstronauts [random.randrange(1,len(listAstronauts))])
print(listAstronauts[random.randrange(1,len(listAstronauts))] == listAstronauts [random.randrange(1,len(listAstronauts))])

#print all astronauts
for x in listAstronauts:
    print(x)
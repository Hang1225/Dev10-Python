class animal:
    def __init__(self,name,age=0,weight=0):
        self.__name = name
        self.__age = age
        self.__weight = weight
    
    @property
    def name(self):
        return self.__name
    
    @property 
    def age(self):
        return self.__age
    
    @property
    def weight(self):
        return self.__weight
    
    def move(self):
        print(f'{self.__name} is moving.')
        return
    
    def eat(self):
        print(f'{self.__name} is eating.')
        return

    def excrete(self):
        print(f'{self.__name} is excreting.')
        return

    def grow(self,weight):
        print(f'{self.__name} is growing.')
        self.__weight += weight
        return self.__weight

class book:
    def __init__(self,title='',author='',language='',genre='',pages=0):
        self.__title = title
        self.__author = author
        self.__language = language
        self.__genre = genre
        self.__pages = pages
        self.__currentPage = 0
    
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def language(self):
        return self.__language
    
    @property
    def genre(self):
        return self.__genre
    
    @property
    def page(self):
        return self.__pages
    
    @property
    def currentPage(self):
        return self.__currentPage
    
    def open(self):
        print(f'The book: {self.title} is opened.')
        return
    
    def flip(self,page):
        print(f'The book is flipped to page {self.currentPage}.')
        self.__currentPage = page
        return
    
    def close(self):
        print(f'The book {self.title} is closed.')
        return
        
class vehicle:
    def __init__(self,make,model,color,yearManufactured,mileage,weight):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__yearManufactured = yearManufactured
        self.__mileage = mileage
        self.__weight = weight

    @property
    def make(self):
        return self.__make
    
    @property
    def model(self):
        return self.__model
    
    @property
    def color(self):
        return self.__color
    
    @property 
    def yearManufactured(self):
        return self.__yearManufactured
    
    @property
    def mileage(self):
        return self.__mileage
    
    @property
    def weight(self):
        return self.__weight
    
    def start(self):
        print('The car is starting.')
        return
    
    def shutoff(self):
        print('The car has shut off.')
        return
    
    def accelerate(self,acceleration):
        print(f'The car is accerating at a rate of {acceleration}/s.')
        return
    
    def brake(self,brake):
        print(f'The car is braking.')
        return
    
    def turn(self,direction=0):
        #0 for left, 1 for right
        if direction == 0:
            print('The car is turning left.')
        elif direction == 1:
            print('The car is turning right.')
        else: print('The car is not turning!')
        return
    
    def reverse(self):
        print('The gear is on reverse now.')
        return


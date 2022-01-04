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
    def __init__(self,make,model,color,yearManufactured,weight):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__yearManufactured = yearManufactured
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

class fish(animal):
    def __init__(self, name,waterType,finLength,age=0, weight=0):
        super().__init__(name, age=age, weight=weight)
        self.__waterType = waterType
        self.__finLength = finLength
    
    @property
    def waterType(self):
        return self.__waterType
    
    @property
    def finLength(self):
        return self.__finLength
    
    def swim(self):
        print('Swimming...')
        return

class person(animal):
    def __init__(self, name, ethnicity, gender, age=0, weight=0):
        super().__init__(name, age=age, weight=weight)
        self.__ethnicity = ethnicity
        self.__gender = gender
    
    @property
    def ethnicity(self):
        return self.__ethnicity
    
    @property
    def gender(self):
        return self.__gender
    
    def talk(self,text):
        print(f'{self.name} says {text}.')
        return

    def sleep(self):
        print(f'{self.name} is sleeping.')
        return

class snake(animal):
    def __init__(self, name, length, venomous = False,age=0, weight=0):
        super().__init__(name, age=age, weight=weight)
        self.__length = length
        self.__venomous = venomous
    
    @property
    def length(self):
        return self.__length
    
    @property
    def venomous(self):
        return self.__venomous
    
    def ecdysis(self):
        print('shredding skin...')
        return
    
    def hibernate(self):
        print('hibernating...')
        return

class textbook(book):
    def __init__(self, ISBN, price = 0, subject = '', title='', author='', language='', genre='', pages=0):
        super().__init__(title=title, author=author, language=language, genre=genre, pages=pages)
        self.__ISBN = ISBN
        self.__price = price
        self.__subject = subject
    
    @property
    def ISBN(self):
        return self.__ISBN
    
    @property 
    def price(self):
        return self.__price
    
    @property
    def subject(self):
        return self.__subject

class addressbook(book):
    def __init__(self, address='', phone = '', title='', author='', language='', genre='', pages=0):
        super().__init__(title=title, author=author, language=language, genre=genre, pages=pages)
        self.__address = address
        self.__phone = phone
    
    @property
    def address (self):
        return self.__address 

    @property
    def phone(self):
        return self.__phone

    def find(self,text):
        print(f'finding {text}...')
        return

class car(vehicle):
    def __init__(self, make, model, color, yearManufactured, weight, mileage,drivetype):
        super().__init__(make, model, color, yearManufactured, weight)
        self.__mileage = mileage
        self.__driveType = drivetype
    
    @property
    def mileage(self):
        return self.__mileage
    
    @property
    def driveType(self):
        return self.__driveType

class bicycle(vehicle):
    def __init__(self, make, model, color, yearManufactured, weight,foldable,gears):
        super().__init__(make, model, color, yearManufactured, weight)
        self.__foldable = foldable
        self.__gears = gears
    
    @property
    def foldable(self):
        return self.__foldable
    
    @property 
    def gears(self):
        return self.__gears
    
    def performTricks(self,trick):
        print(f'Performing trick: {trick}.')
        return

class hotairballoon(vehicle):
    def __init__(self, make, model, color, yearManufactured, weight,basketmaterial,evelopeDiameter):
        super().__init__(make, model, color, yearManufactured, weight)
        self.__basketMaterial = basketmaterial
        self.__envelopeDiameter = evelopeDiameter
    
    @property
    def basketMaterial(self):
        return self.__basketMaterial
    
    @property
    def envelopeDiameter(self):
        return self.__envelopeDiameter
    
    def rise(self):
        print('The balloon is rising...')
        return
    
    def descend(self):
        print('The balloon is descending')

class boat(vehicle):
    def __init__(self, make, model, color, yearManufactured,, weight,breadth,length):
        super().__init__(make, model, color, yearManufactured, weight)
        self.__breadth = breadth
        self.__length = length
    
    @property
    def breadth(self):
        return self.__breadth
    
    @property
    def length(self):
        return self.__length
# class Dog():
#     '''
#     Class Object Attributes are defined before the __init__ method and are the same
#     for every instance of the class.
#     '''
#     species = 'Mammal'
#
#
#     '''
#     self keyword connects method to this instance of the class
#     Init is basically the constructor for the class and is called automatically when
#     an object of the class is created.
#     '''
#     def __init__(self, breed, name, spots):
#         self.breed = breed #String expected
#         self.name = name #String expected
#         self.spots = spots #boolean expected
#     '''
#     Methods are functions defined in the body of a class and are used to perform
#     operations that sometimes utilize the attributes of the object that we created.
#     '''
#     def bark(self):
#         print("WOOF! My name is {}.".format(self.name))
#     pass
# my_dog = Dog("German Shepherd", 'Toby', False)
# type(my_dog)
# my_dog.breed
# my_dog.name
# my_dog.spots
# my_dog.species
# my_dog.bark()


class Circle():
    # CLASS ATTRIBUTES
    pi = 3.14

    # Default values can be overwritten
    def __init__(self, radius = 1):
        self.radius = radius

    # Method
    def get_circumference(self):
        return self.radius*self.pi*2

my_circle = Circle()

my_circle.pi
my_circle.get_circumference()

# '''
# INHERITANCE AND POLYMORPHISM
# '''
class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")
# '''
# Dog class will inherit from the base class Animal.
# '''
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    # Functions that are inheritted can be overwritten in the child class
    def who_am_i(self):
        print("I am a dog.")
    # You can also create new functions in the child class that the parent class can't use
    def bark(self):
        print("WOOF!")

mydog = Dog()
mydog.who_am_i()
mydog.bark()
myanimal = Animal()
# myanimal.bark() doesn't work

# POLYMORPHISM
class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"
class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"
niko = Dog("Niko")
felix = Cat("Felix")
print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)
# Becuase both classes, Dog and Cat, share a method with the same name we can use a funciton
# or iterate through them as a list and call that method from both classes

# INHERITANCE is usually used with an abstract class that is designed to never be instantiated but
# to be used as a base class
class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method!")
fred = Animal("Fred")
class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"
fido = Dog("fido")
fido.speak()

# OOP HOMEWORK AND CHALLENGE
import math
class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        coor1x,coor1y = self.coor1
        coor2x, coor2y = self.coor2
        return math.sqrt((coor2x-coor1x)**2 + (coor2y-coor1y)**2)
    def slope(self):
        coor1x,coor1y = self.coor1
        coor2x, coor2y = self.coor2
        return (coor2y-coor1y)/(coor2x-coor1x)
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return (math.pi * self.radius**2)*self.height
    def surface_area(self):
        return 2*(math.pi*self.radius*self.height)+self.volume()
c = Cylinder(2,3)
c.volume()
c.surface_area()

# CHALLENGE

class Account:
    def __init__(self, owner = " ", balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
        return "Deposit Accepted"
    def withdraw(self, money):
        if self.balance - money > 0:
            self.balance -= money
            return "Withdrawal Accepted"
        else:
            print("EXCEEDS CURRENT BALANCE.\nCurrent balance is: {}".format(self.balance))
    def __str__(self):
        return "Account owner: " + self.owner+"\nAccount balance: $"+str(self.balance)
acct1 = Account("Jose", 100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)

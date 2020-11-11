class Dog():
    '''
    self keyword connects method to this instance of the class
    Init is basically the constructor for the class and is called automatically when
    an object of the class is created.
    '''
    def __init__(self, breed):
        self.breed = breed
    pass
my_dog = Dog("German Shepherd")
type(my_dog)
my_dog.breed

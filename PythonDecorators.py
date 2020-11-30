###     Funcitons are objects that can be passed into other objects     ###

def func():
    return 1

def func2():
    return 2

def hello(name = 'Jose'):
    print('The hello function has been executed.')

    def greet():
        return "\tThis is the greet() function inside hello."

    def welcome():
        return "\t\tThis is welcome() inside hello()!"

    print("I am going to return a function.")

    if name == 'Jose':
        return greet
    else:
        return welcome

hello()
# Use the fact that the hello() function returns its two local functions based on the name
# that is passed in to assign those functions to variable.

my_new_func = hello() # Because the default name is 'Jose' this will assign greet()
print(my_new_func())

my_other_func = hello("David")

def cool():
    def super_cool():
        return 'I am very cool!'
    return super_cool
some_func = cool()
some_func()


###     Passing in a function as an argument       ###

def hello():
    return 'Hi Jose!'
def other(some_def_func):
    print("Other code runs here.")
    print(some_def_func())

other(hello)
def new_decorator(original_func):

    def wrap_func():
        '''
        this is the extra functionality that you want to wrap the original function with
        '''
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code eecuted after the original function')
    return wrap_func

# decorated_func = new_decorator(func_needs_decorator)
# print(decorated_func())

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")
func_needs_decorator()

# This file will contain the lessons for python methods and functions.
# Functions
# Creating clean repeatable code is a key and effective part of being a programmer
# Functions allow us to reapeat multiple lines of code without rewriting them over and over
# Functions in python require specific syntax that includes the 'def' keyword, correct indentation and proper structure
def name_of_funciton(): #in general python uses what is called snake casing for the names of functions, all lowercase with underscores btwn words
    '''
    Docstring is a comment that explains the function and what it does
    '''
    print('hello')

name_of_funciton()

# typically functions will not be this simple and will use the 'return' keyword to return some result where the function is called
# this allows the result to be saved to a variabl.

def add_function(num1,num2):
    return (num1+num2)

result = add_function(10, 35)
print(result)

def say_hello():
    print('Hello')
say_hello()

def say_hello(name= 'Default'):# the default will help to avoid the error of leaving the param blank when calling the funciton
    print(f'Hello {name}')
say_hello('Evan')

# RETURN True if any number in a list is even
def check_even_list(num_list):
    for num in num_list:
        if num%2 == 0:
            return True
        else:
            pass
    return False
check_even_list(list(range(1,101,2)))

#now return all even numbers in a list
def check_even_list(num_list):
    #place holder variable are defined at the top of a function
    even_numbers = []
    for num in num_list:
        if num%2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers #will return a list of even numbers or an empty list if there are none
check_even_list(list(range(1,101,3)))

# unpacking tuples with functions
work_hours = [('Abby',100),('Billy', 4000),('Cassie',800)]
def employee_check(work__hours_list):
    '''
    This function will take is a list of tuples with employee names and the hours that
    they have worked.  It iterates through the list and determines which employee worked the
    most hours making them the employee of the month.  The function returns this as a tuple
    that can be unpacked and use accordingly.
    '''
    current_max = 0
    employee_of_month = ''
    for employee,hours in work__hours_list:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)

name,hours = employee_check(work_hours)

print(f'The employee of the month is {name} with {hours} hours!')

# create a few functions to mimic three cup monte
example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
example

def shuffle_list(myList):
    shuffle(myList)
    return myList
result = shuffle_list(example)
result

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number 0, 1, or 2: ')
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong guess!")
        print(mylist)

# Now for the actual logic behind the game

# Initial List
startlist = ['','O','']
# Mixed up list
shuffled_list = shuffle_list(startlist)
# USER GUESS
guess = player_guess()
# Guess Check
check_guess(shuffled_list, guess)

# *args and **kwargs, stands for arguments and keyword arguments
def my_func(a, b):
    '''
    returns 5% of the sum of a and b
    '''
    return sum((a,b)) * 0.05
my_func(40,60)
# when a function parameter starts with * it allows for as many numbers as you want to pass in and encases them in a tuple

def my_func(*args):
    return sum((args)) * 0.05
my_func(5,5,5,5,5,5,5,5,5,5)

def kwargs_func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here.')
# Parameters that start with ** will return them as a dictionary

kwargs_func(fruit = 'apple', veggie = 'lettuce')

# using both
def my_func(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))
my_func(10, 20, 30, fruit = 'orange', food = 'eggs', animal = 'dogs')

# This lets you take in an arbitrary amount of arguments and keyword arguments.

def myfunc(mystring):
    newstring = ''
    x=0
    while x < len(mystring):
        if x%2==0:
            newstring = newstring + mystring[x].lower()
            x+=1
        else:
            newstring = newstring + mystring[x].upper()
            x+=1
    return newstring

myfunc('Anthropomorphism')

# FUNCTIONS PRACTICE PROBLEMS
# WARMUP
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    list = [word[0] for word in text.split()]
    if list[0].lower() == list[1].lower():
        return True
    else:
        return False
animal_crackers("Levelheaded Llama")
animal_crackers('Crazy Kangaroo')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(a,b):
    if a==20 or b==20:
        return True
    elif sum((a,b)) == 20:
        return True
    else:
        return False
makes_twenty(20,10)
makes_twenty(2,3)
makes_twenty(5,15)
makes_twenty(25, -5)

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
def old_macdonald(name):
    newName = ''
    x = 0
    while x < len(name):
        if x==0 or x==3:
            newName = newName + name[x].upper()
            x += 1
        else:
            newName = newName + name[x]
            x+=1
            pass

    return newName
old_macdonald('macdonald')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
def master_yoda(text):
    mylist = text.split()
    mylist.reverse()
    reversed_string = " ".join(mylist)
    return reversed_string
master_yoda('I am home')
master_yoda('we are ready')

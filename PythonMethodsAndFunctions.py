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

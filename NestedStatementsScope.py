# NESTED STATEMENTS AND SCOPE
x = 25
def printer():
    x =50
    return x
print(printer())
# LEGB RULE FORMAT
# LOCAL, ENCLOSING FUNCTION LOCAL, GLOBAL, BUILT IN
name = 'THIS IS A GLOBAL STRING' #Global

def greet():
    name = 'Sammy'#Enclosing function local, if commented out hello would then look globally

    def hello():
        name = "I'm a local"
        print('Hello '+name)#First searches locally within the function for the definition of name

    hello()
greet()

x = 50
def func(x):
    print(f'X is {x}')
    x = 200 #Local reassignment
    print(f'I just locally changed x to be {x}')
func(x)
# the local reassignment only has scope within the function.  Therefore it can't reach the global variable
def func2():
    global x #allows the function to change the global variable using the global keyword
    print(f'X is {x}')
    x = 200 #Local reassignment
    print(f'I just locally changed global x to be {x}')
func2()
print(x)

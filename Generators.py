import math
import random
def create_cubes(n):
    '''
    creates cubes from 0 to n
    '''
    for x in range(n):
        # yield keyword makes this funciton a generator
        yield(int(math.pow(x,3))) #cubes x could also use import math and us pow

for x in create_cubes(10):
    print(x)
# Create a fibonacci sequence up to n
def gen_fib(n):
    '''
    will generate a fibonacci sequence up to n
    using the generator instead of creating a list is much more memory
    efficient. This is because as a list the entire sequence up to n is
    created and then stored in memory then returned. As a generator using
    the yield keyword, it will wait until the next call to generate the
    next number.
    '''
    a = 0
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b
for x in gen_fib(10):
    print(x)

def simple_gen():
    for x in range(3):
        yield x
for num in simple_gen():
    print(num)

g = simple_gen()
g
next(g)
next(g)
next(g)

s = 'hello'
for letter in s:
    print(letter)
s_iter = iter(s) # this converts an object that is iterable into an iterator
next(s_iter)     # This allows us to use next on the object.

### Iterators and Generators Homework ###

def gensquares(N):
    '''
    generates the squares of number from 0 up to # N
    '''
    for x in range(N):
        yield int(math.pow(x,2))
for num in gensquares(10):
    print(num)

def rand_num(low,high,n):
    '''
    create a generator that yields n random numbers between a low and a high number
    '''
    x = 0
    while x < n:
        yield random.randint(low,high)
        x+=1
for x in rand_num(1,10,12):
    print(x)

    

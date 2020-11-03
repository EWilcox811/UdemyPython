def square(num):
    return num**2
my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
    print(item)
list(map(square,my_nums))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

name = ['Andy','Eve','Sally']
list(map(splicer,name))
# When using the map function, you enter the function name as an argument without the ()
# You aren't calling the funciton in the map call, map calls it later. If you do enter ()
# you will receive a type error

# FILTER funciton
def check_even(num):
    return num%2==0

mynums = [1,2,3,4,5,6]
list(filter(check_even, mynums))

# LAMBDA EXPRESSIONS
def square(num):
    result = num ** 2
    return result
# Turning this into a lambda EXPRESSION
# Also known as an anonymous function
list(map(lambda num: num**2, mynums))
# Typically this is used in conjunction with other functions like map and filter.
list(filter(lambda num:num%2==0, my_nums))
list(map(lambda name:name[::-1], name))

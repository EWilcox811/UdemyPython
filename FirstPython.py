print('hello world')
mystring = "Hello World"
print(mystring[0])
print(mystring[8])
print(mystring[-2])
print(mystring[-1])
print(mystring[0:4])
v = [2,1,12,13,8,6,7,9,10,5]
v[2:10:3]
v[9:3:-2]
mystring.lower()
print(mystring)
mystring.upper()
mystring.split()
#print formatting for strings.
#known as string interpolation
print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

#float formatting follows (value:width.precision f)
result = 100/777
result
print("The result was {r}".format(r=result))
print("\nWith Formatting\n")
print("The result was {r:1.3f}".format(r=result))

#fstrings, formatted string literals
name = 'Jose'
print(f'Hello his name is {name}')

name = 'Sam'
age = 3
print(f'\n{name} is {age} years old.')

# Lists - ordered sequences that can hold a variety of objects
#       - use [] brackets and commas to separate objects in the Lists
#       - similar to strings, Lists support indexing and slicing.
# Lists can be nested and have a variety of useful methods that can be called off of them.
myList = [1,2,3]
# Lists do not have to be all one type, can be mixed objects.
len(myList)
myList[0]
myList[1:]
anotherList = [4,5]
myList + anotherList
# Unlike strings, you can change the elements.
myList[0] = 'one'.upper()
print(f'\nMy List: {myList}')
myList = myList + anotherList
myList.append('Six')#append method adds an item to the end of the list.
myList.append(7)
print(f"\nMy List after appends: {myList}")
# Popping an item from a list will by default give you the last item in the list.
# However you can put an index in the pop method and it will pop out the desired object.
# When popping an item it does remove it from the list.
print(f'\nItem popped from myList:\t{myList.pop(0)}')
print(f'\nmyList after the pop:\n{myList}')
# Sort and Reverse
newList = ['a','e','x','b','c']
numList = [4,1,8,3]
print(f'\n\nUnsorted list of chars:\t\t{newList}')
print(f'\n\nUnsorted list of integers:\t{numList}')
newList.sort()
numList.sort()
print(f'\nSorted list of chars:\t\t{newList}')
print(f'\nSorted list of integers:\t{numList}')
print('\n\n')
# sort method is an in place method so you cannot assign it to a new list
# because it doesn't return anything that can be assigned to a variable.
# reverse is the same way, it is in place and doesn't return anything that can
# be assigned to a variable
newList.reverse()
numList.reverse()
print(f'Reverse list of chars:\t\t{newList}')
print(f'\nReverse list of integers:\t{numList}')
# basics of lists completed most important methods
#       append, pop, sort, reverse

# Dictionaries
# unordered mappings for storing objects.
# uses a key value pairing instead of indexing like lists.
# allows the useer to quickly grab objects without needing to know an index location.
# When should you use a list or dictionary?
# Dictionaries when you need to quickly retrieve a value without knowing its indexing
# Lists can retrieve objects off location and can be ordered/nSorted
myDict = {'key1':'value1', 'key2':'value2'}
myDict['key1']
priceLookup = {'apple':2.99, 'oranges':1.99, 'milk':5.80}
print('\n\nDictionary use:\n')
print(f'Dictionary:\t{priceLookup}\n')
#assigning cost to variables
appleCost = priceLookup['apple']
orangeCost = priceLookup['oranges']
milkCost = priceLookup['milk']
#printing costs of each individual item.
print(f'Price of an apple:\t\t${appleCost:1.2f}')
print(f'\nPrice of an orange:\t\t${orangeCost:1.2f}')
print(f'\nPrice of a carton of milk:\t${milkCost:1.2f}')

# Dictionaries can also hold lists or even other dictionaries.
d = {'k1' : 123, 'k2' : [0,1,2], 'k3':{'insideKey':100}}
#test
d2 = {'key1':[1,5,3,4,7,2]}
sortedList = d2['key1'].sort() #assignment doesn't work because sort is an in place method
sortedList = d2['key1']#this assignment assigns the sorted list succesfully
print(f'\nSorted list from dictionary d2:\t{sortedList }\n')

#useful dictionary methods
print(f'\n{d.keys()}')#returns the keys
print(f'\n{d.values()}')#returns the values
print(f'\n{d.items()}')#returns the 'key':value pairs

# Tuples in Python
# Similar to lists but with the key difference of immutability.
# Once an element is inside of a tuple it can not be reassisgned

t = (1,2,3)
myList = [1,2,3]

print(type(t))
print(type(myList))

print(len(t))

print(t[0])# tuples support indexing
print(t[::-1])# they also support slicing, this prints a reverse of the tuple.
# The count method will tell you how many times a specific item occurs in your tuples
tup = (1,1,1,2,2,2,2,3,3,4,5)
print(tup.count(2))# prints out 4
# The index method will tell you at what index an item first occurs in the tuple
print(tup.index(3))# prints out 7
print(tup.index(1))# prints out 0
# Tuple immutability
# tup[0] = 'new' this doesn't work because it is immutable and you can't reassign the object
# great for data integrity.

# Sets
# Unordered collection of unique elements
mySet = set()
mySet.add(1)
print(mySet)
mySet.add(2)
mySet.add(2)# won't be added to the set because it is already there.
myList = [1,1,1,1,1,2,2,2,3,3,3,3]
print(f'List before casting to set:\n{myList}\nAfter being cast to a set: ')
print(set(myList))# cast the list as a set to obtain the unique items.

# Booleans
# operators that convey true or false statements
# great for control flow and logic
type(False) #return bool
print(1 > 2) # prints False
print(1==1) # prints true

# File I/O basics
myFile = open('test')
print(myFile.read())# once completed the cursor is at the end of the File
myFile.seek(0)# resets the cursor to the beginning of the file
contents = myFile.read()
myFile.seek(0)
contentsList = myFile.readlines()# will return the contents of the file as a list if there is more than one line.
# you can open a file from anywhere on your computer you just have to include the entire file path in the .open()
# remember to close the file when you are finished with it.
myFile.close()
#use with as to avoid errors
with open('test') as myNewFile:
    contents = myNewFile.read()#no need to close the file when using with as
    print(contents)
# write to files and overwrite files
with open('test', mode = 'r') as myFile:
    contents = myFile.read()
# if you change the mode to w it will write and overwrite files that already exist
# changing the mode to a will append to the end of an existing file.
with open('test', mode = 'a') as f:
    f.write('\nSecond on Second')
with open('myNewFile.txt', mode = 'w') as f:
    f.write("This is a new file created in Python.\nThis is the second line in the new File.")
with open('test') as r:
    print(r.read())
with open('myNewFile.txt', mode = 'r') as f:
    print(f.read())
# Chaining comparison with and without the keywords and, or, not
print(1<2<3)# prints true
print(1<2>3)# prints False
# from this point on installed the hydrogen package and ipykernel and will no longer need to use print
x=1
x
'h'=='h' and 2==2
1==1 or 2==2
100==1 or 2==2
# Using the keywords help with the readability of the code and is better than not using it
# The not operator returns you the opposite boolean. Useful for control flow
not (1==1)

# If, elif, else statements
# control flow syntax in python makes use of colons and whitespace easily readible and prototyped
# if condition:
#     run this code
# else:
#     run this code
if (3<2):
    print('It\'s True')
elif (3>2):
    print('Now it is True')
else:
    print('It\'s False')
name = 'Sammy'
if name == 'Frankie':
    print('Frankie')
elif name == 'Sammy':
    print('Hello Sammy')
else:
    print('What is your name?')

# For loops, used with iterable objects such as iterating through every character in a String

myIterable = [1,2,3,4,5,6,7,8,9,10]
for numbers in myIterable:
    print(numbers)
for numbers in myIterable:
    if (numbers % 2 ==0):
        print(f'Even Number:{numbers}')
    else:
        print(f'Odd Number:{numbers}')

# Tuple unpacking
myList = [(1,2),(3,4),(5,6)]
for (a,b) in myList:
    print(a)
    print(b)
# If not unpacked, it will print the tuples themselves
for tup in myList:
    print(tup)
# Iterating through a Dictionary.  You can do the same unpacking as a Tuple.
d = {'k1':1, 'k2':2, 'k3':3}
for item in d.items():
    print (item)
for key,value in d.items():
    print(f'Key = {key} \tValue = {value}')

# While loops, continually execute while some condition is true
# while someBooleanCondition:
#     do something
# while loops in python can be combined with else statements
# while someBooleanCondition:
#     do something
# else:
#     do something different
x=0
while x<=5:
    print(f'Current value of x = {x}')
    x += 1
# keywords break, continue and pass
# break: breaks out of the current closest encosing loop
# continue: Goes to the top of the closest enclosing loop
# pass: Does nothing at all
x = [1,2,3]
for item in x:
    pass #used to avoid syntax error as a place holder if you want to come back to this
# continue
myString = 'Sammy'
for letter in myString:
    if letter == 'a':
        continue #when we hit the letter 'a' it will go back to the top of the loop and not print out 'a'
    print(letter)
# break
for letter in myString:
    if letter == 'a':
        break #when we hit the letter 'a' it will break out of the loop
    print(letter)
x = 0
while x<5:
    if x==2:
        break #when x = 2 it will break out of the loop and only print 0 and 1
    print(x)
    x+=1

# Useful operator in python
# range function
mylist = [1,2,3]
for num in range(10):# range(start, stop, step) is a generator
    print (num)
# when range is casted to a list it will generate the list
# the stop argument in range(start,stop,step) is non inclusive
mylist = list(range(0,11,2))
mylist #mylist is [0,2,4,6,8,10]

# enumerate
indexCount = 0
for letter in 'abcde':
    print(f'At index {indexCount} the letter is {letter}.')
    indexCount+=1
# such a common operation that enumerate can replicate this
indexCount = 0
word = 'abcde'
for item in enumerate(word):#this will print out tuples of word with the (index, letter)
    print(item)
#this can be unpacked using tuple unpacking
for index,letter in enumerate(word):
    print(f'Letter {letter} is at index {index}')

# zip function will zip together multiple lists.  It will only zip together as many elements as the smallest list
# the lists are zipped together in the form of tuples.
firstList = list(range(1,6))
secondList = ['a','b','c','d','e']
thirdList = list(range(7,10))
zip(firstList, secondList)
for ite in zip(firstList, secondList, thirdList):# because third list only has 3 items, only 3 tuples are returned
    print(ite)
# if you just want the list you can cast it to list
zippedList = list(zip(firstList,secondList,thirdList))
zippedList

# in operator can be used to check if an item is in an iterable item ie list, string, dictionary...
'a' in 'a world'
'mykey' in {'mykey':345}
d = {'mykey':345}
345 in d.values()
345 in d.keys()

# mathematical library, min, max, random
x = list(range(0,101,10))
x
min(x)
max(x)

from random import shuffle
shuffle(x)#shuffle is an in palce function and returns nothing and only affects the list passed into it.
x
x.sort()# puts list back in numerical order
x
shuffle(x)
x
x.sort()

from random import randint
randint(0,100)

# excepting user input
result = float(input('Enter a number here: ')) # be careful because everything is saved as a string must be cast to be an actual number
result

#list comprehension

mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
mylist

# more efficient way aka less code not less memory
mylist = [letter for letter in mystring]
mylist
# mylist = ['element' for 'element' in 'some string or iterable object']
# this is the same as running a for loop to append the elements in the iterable object to a list
# can also be used to create a list of numbers withing a certain range
mylist = [x for x in range(0,11)]
mylist

# you can even begin to perform operations on the variable as you append it to the list
# i.e. appending the square of all the numbers in a range

mylist = [num**2 for num in range(0,11)]
mylist

# can also add in if statements to the assignment statements
# i.e. grabbing the even numbers in a range

mylist = [num for num in range(0,11) if num%2 == 0] #this will only append to the list if True
mylist

# more complex arithmetic
celsius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
fahrenheit

# you can do if else chains in the assignment but it can become an ugly one liner
# don't do this hurts code readability
results = [x if x%2 ==0 else 'ODD' for x in range(0,11)]
results
# UGLY

# you can also do nested loops in a list comprehension but also can become quite complicated and hard to read
mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
mylist
# same as
mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
mylist

# Python statements assessment test

st = 'Print out only the words that start with s in this sentence'
list = st.split()
list
for word in list:
    if word[0]=='s':
        print (word)
for num in range(0,11):
    if num%2 == 0:
        print(num)

divThreeList = [num for num in range(1,51) if num%3 == 0]
divThreeList

st = 'Print ever word in this sentence that has an even number of letters'
stList = st.split()
for word in stList:
    if(len(word)%2==0):
        print('even!')

for num in range(1,101):
    if(num%3==0 and num%5==0):
        print('FizzBuzz')
    elif(num%3==0):
        print('Fizz')
    elif(num%5==0):
        print('Buzz')
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'
firstLetters = [word[0] for word in st.split()]
firstLetters

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

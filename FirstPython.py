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

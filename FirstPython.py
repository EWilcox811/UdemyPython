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

#Lists - ordered sequences that can hold a variety of objects
#      - use [] brackets and commas to separate objects in the Lists
#      - similar to strings, Lists support indexing and slicing.
#        Lists can be nested and have a variety of useful methods that can be called off of them.
myList = [1,2,3]
#        Lists do not have to be all one type, can be mixed objects.
len(myList)
myList[0]
myList[1:]
anotherList = [4,5]
myList + anotherList
#        Unlike strings, you can change the elements.
myList[0] = 'one'.upper()
print(f'\nMy List: {myList}')
myList = myList + anotherList
myList.append('Six')#append method adds an item to the end of the list.
myList.append(7)
print(f"\nMy List after appends: {myList}")
#        Popping an item from a list will by default give you the last item in the list.
#        However you can put an index in the pop method and it will pop out the desired object.
#        When popping an item it does remove it from the list.
print(f'\nItem popped from myList:\t{myList.pop(0)}')
print(f'\nmyList after the pop:\n{myList}')
#        Sort and Reverse
newList = ['a','e','x','b','c']
numList = [4,1,8,3]
print(f'\n\nUnsorted list of chars:\t\t{newList}')
print(f'\n\nUnsorted list of integers:\t{numList}')
newList.sort()
numList.sort()
print(f'\nSorted list of chars:\t\t{newList}')
print(f'\nSorted list of integers:\t{numList}')
print('\n\n')

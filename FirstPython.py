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

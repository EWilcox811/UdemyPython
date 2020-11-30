### Python Collections Module ###
import collections
from collections import Counter
mylist = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,]
# Counts the number of unique items in a list or iterable object and return a special Counter object
Counter(mylist)
from collections import defaultdict
d = {'a':10}
d
d['a']
d['WRONG']
# default dictionaries from the collections module will not give you a KeyError
# instead if you ask for a key that is not present within the dictionary, it will
# create an instance with a default value associated to that key.
d = defaultdict(lambda: 0)
d['correct'] = 100
d['WRONG KEY']
d

# Named Tuple
from collections import namedtuple
#just your standard tuple you need to know what index the item you want is at.
mytuple = (10,20,30)
mytuple[0]

# very similar to a OOP creating your own object
dog = namedtuple('Dog',['age','breed','name'])
sammy = dog(age = 5, breed = 'Husky', name = 'Sam')
sammy
sammy.age
sammy.breed

### Python Shutil and OS module ###
import os
f =  open('C:/Users/vein8/Desktop/Coding/Python/python/test.txt', 'w+')
f.write('This is a test string.')
f.close()
os.chdir('C:/Users/vein8/Desktop/Coding/Python/python/')
os.getcwd()
os.listdir()
import shutil
shutil.move('test.txt', 'C:/Users/vein8/Desktop')
shutil.move('C:/Users/vein8/Desktop/test.txt','C:/Users/vein8/Desktop/Coding/Python/python/')
os.listdir()

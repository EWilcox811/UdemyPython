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
# Safe way to delete a file using send2trash
import send2trash
send2trash.send2trash('test.txt')

fp = os.walk('C:/Users/vein8/Desktop/Coding/Python/', topdown=True)


###     Datetime module     ###
import datetime
mytime = datetime.time(2,20)
mytime.minute
mytime.hour
print(mytime)


###     Math and Random Modules     ###
import math
import random
value = 4.35
math.floor(value)
math.ceil(value)
round(value)
math.pi
from math import pi
math.e
math.inf
math.nan

##  checkout the numpy library
math.log(math.e)
math.log(10,10)
math.log(100,10)


###     how to get the same set of random numbers  ###
random.randint(0,100)
random.seed(101)
random.randint(0,100)

mylist = list(range(0,20))
random.choice(mylist)

# 5 random numbers from the list
# sample with replacement and without
# with replacement
random.choices(population = mylist, k=10)
# some numbers duplicate because we are sampling with replacement
# without replacement
random.sample(population = mylist, k=10)
# no numbers are repeated because once picked it can't be picked again
# shuffling a list
random.shuffle(mylist)
mylist

# every number between 0-100 has the same likliness of being chosen
random.uniform(0,100)
# normal or gaussian distribution
random.gauss(mu = 0, sigma = 1)


###     Python Debugger     ###
x = [1,2,3]
y = 2
z = 3
import pdb

result_one = y+z
pdb.set_trace()
result_two = x+y



###     Python Regular Expressions      ###
# regex allows us to search for a general pattern within text data.
# construct a generalized pattern to search for matches
# phone number regex
import re
phone = r"(\d{3})-\d{3}-\d{4}"
text = "The agent's phone number is 408-555-1234. Call soon!"
pattern = 'phone'
match = re.search(phone, text)
match.span()
match.start()
print(match.group())


###     Timing your code       ###
import time
import timeit

def func1(n):
    return[str(num) for num in range(n)]
def func2(n):
    return list(map(str,range(n)))
# Timing your code the hard way. For code that runs fast this isn't precise
# grab current time
start_time = time.time()
# runcode
result = func1(1000000)
#grab time after code finishes
end_time = time.time()
time_elapsed = end_time-start_time
print(time_elapsed)

# grab current time
start_time = time.time()
# runcode
result = func2(1000000)
#grab time after code finishes
end_time = time.time()
time_elapsed2 = end_time-start_time
print(time_elapsed2)

# Using the timeit module
stmt='''
func1(100)'''
setup='''
def func1(n):
    return[str(num) for num in range(n)]'''
timeit.timeit(stmt, setup, number=1000000)
stmt2 = '''
func2(100)'''
setup2 = '''
def func2(n):
    return list(map(str,range(n)))'''
timeit.timeit(stmt2, setup2, number = 1000000)


###     Unzipping and Zipping files     ###
f = open('file1.txt', mode='w+')
f.write('One File')
f.close()

f = open('file2.txt', mode='w+')
f.write('Two File')
f.close()

import zipfile
comp_file = zipfile.ZipFile('comp_file.zip',mode='w')
comp_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip',mode='r')
zip_obj.extractall('extracted_content')
import shutil
import os
dir_to_zip = os.getcwd() + '\extracted_content'
output_file = 'example'
shutil.make_archive(output_file,'zip',dir_to_zip)
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')
import send2trash
send2trash.send2trash(os.getcwd()+'\final_unzip/')

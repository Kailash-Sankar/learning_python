'''
installing python packages
go to : https://pypi.python.org/
wheel/egg - packaging techniques

pip install package-name

C://Python27/Scripts
pip install xlrd

module - a reusable python file
package - a collection of modules. folder

all 3rd party stuff - site-packages

import sys
sys.path

PYTHONPATH - define a folder for python to search

after making a package, pass it to setup.py and it'll create a pip ready package

'''
import magic
import magic.kadabra

print(dir(magic))
print(dir(magic.kadabra))
print(dir(magic.kadabra.kadabra))

magic.hat()
magic.magik_time(4, 5)

magic.kadabra.flash()

magic.kadabra.kadabra.smoke()

print("---")
# random
import random

for x in range(10):
    print(random.random(),end=' ')
print

for x in range(10):
    print(random.randint(50, 150),end=' ')
print

for x in range(10):
    print(random.randrange(50, 150),end=' ')
print

help(random.randrange)
help(random.randint)

print("---")
x = [56, 78, 34, 67, 33, 355, 66]
print(random.choice(x))
print(random.sample(x, 3))

random.shuffle(x)
print(x)
random.shuffle(x)
print(x)
print(x.pop())
print("---")

# date time
from datetime import datetime, date

print(dir(datetime))
print(dir(date))

x = datetime.now()
print(type(x))
print(x.day, x.year, x.weekday())
print(x.strftime('%A %d. %B %Y'))
print(x.strftime('%d/%m/%y'))
print("-*-")

ind = date(2016, 10, 15)
today = date.today()

print(today - ind)
print((today-ind).days)

print(date.today().weekday())
print("-**-")

import time

start = time.time()
for x in range(10000000):
    y = x * x
end = time.time()

print(end - start)

time.sleep(1)
print('shroooom')

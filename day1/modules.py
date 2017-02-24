# returns the list of available python modules
# help('modules')

import math

print math.sin(45), math.tan(45)

# returns list of available methods
print dir(math)

# returns help for a specific method
help(math.sin)

# ways to import modules

# generic import
import random

print random.random()

# function import
from math import cos, tan

print cos(90)

# universal import
from math import *

print factorial(5)

# function import with rename
from math import factorial as fact

print fact(9)

# import with module rename
import math as m

print m.tan(90)

# returns global namespace
print globals()

print __name__
print __file__

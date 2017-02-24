import megamod

dir('megamod')

print megamod.name
print megamod.pow(5)

# if the local program name is same as module name then the program will load itself
# and throw and error
# after renaming the file, make sure to remove the compiled file

import random
print random.randint(1,10)
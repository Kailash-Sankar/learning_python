# regex

import re

# find
r = re.findall('\d+', '13 blue pens, 9 balls, 6 books and 20 rupees')
print 'find', r

# split
r = re.split('[,:-]', 'Ramesh,223-rsannareddy@yahoo.com:Trainer')
print 'split', r

# match
r = re.match('ba', "ba ba blacksheep ba ba blacksheep")

print 'match', r, bool(r)
# only matches from the begining of the string!!
r = re.match('black', "ba ba blacksheep ba ba blacksheep")
print 'match', r, bool(r)

# search
r = re.search('\w{10}', "ba ba blacksheep ba ba blacksheep")
print 'search', r

print r.group()  # returns the matched string
print r.span()  # returns slicable index


#sub is working like it has '+'
print re.sub('\d','*','this is the pin 2020')

# compile a regex and use it
mobile = re.compile("[789]\d{9}")
print mobile.findall("9885970033 8945 9292929")


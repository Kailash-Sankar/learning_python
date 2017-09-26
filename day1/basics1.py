print( 'Learning Python - Day 1')

# data types
# multi line strings
dt = [1,2.567,"shiver"'me','''
timbers
''',
True,
False,
[],(),{},{2,4,5},
None
]

# loop
for x in dt:
	print( x,' is of type ', type(x))

# boolean values and bool test
bt = [False,None,0,0.0,(),{},[],-6]

for x in bt:
	print(( x,' bool ', bool(x)))

# conditionals inside print()
# observe the behaviour
print( "---")
print( 3 or 4)
print( 3 and 4)
print( 0 or 3 or 4)
print( 3 and 0 and 4)

# multiple assignments in one line
c,d = [6,7],[6,7]
e = c;

# checks in print()
print( "---")
print( id(c),id(d),id(e))
print( c == d)
print( c is d)

print( c == e)
print( c is e)

# c and e point to the same location in memory
e.append(2);
print(c,e);

# references and ref count
import sys

a = [1,2,3,4,5]
b = a
c = b
d = c
print( "---")
# the count is one higher, includes the temporary reference passed on the function
print( sys.getrefcount(a))


# length, min, max
# slice and dice
a = [4,5,6,7,8,9,10]
print( "-*-")
print( len(a), min(a), max(a))
print( a[2:3], a[4:], a[:4], a[:])
print( a[4:10])
print( a[-1], a[-3:-1])  # reverse index, but L => R
''''
does not include the limit specified on the right. prints till the limit index
'''
# pay attention
print( '-**-')
print( a[0:10:2], a[0:10:3])
print( a[:], a[::], a[::1])   # prints every element

print( a[::-1])   # prints every element in reverse
print( a[3:1:-1])  # reverse index, reverse lookup

print( "-***-")
a[3:5] = [15,67,32]
print(a)
a[3:5] = []
print(a)

# list operations
b = [6,7,8,9]
print( "-%-")
print(b)
b.append(10)
b.insert(0,5)
b.append(7)
b.remove(7)  # removes first occurance, doesn't return a value
print(b)

b.extend([88,99])
l = b.pop()
print(b, l)

b[len(b):] = [90,92,33]
print(b)

#sorting
b.reverse()
print(b)

b.sort()
print(b)

print(b.index(92))
print(b.count(99), b.count(90))

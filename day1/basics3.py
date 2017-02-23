# tuples
a = (567, 67, 77, 45, 1)

print len(a), type(a)
print a[2:], min(a), max(a)

b = ('hello', 'world', 'foo', 'bar', 'tuna')
print min(b), max(b)
print a.index(67)

# to make a single element tuple, add a comma
x, y, z = (4), ('aloha'), (4,)
print type(x), type(y), type(z)

g = 6, 7, 4, 5, 67
print type(g)
print "---"

# sets
t = {4, 5, 6, 34, 4, 5, 6}
print type(t), t
t.add(89)
t.add(89)
print t

s1 = {'apple', 'mango', 'banana', 'grape', 'tomato'}
s2 = {'potato', 'tomato', 'cabbage'}

print s1.intersection(s2)
print s2.union(s1)
print s1 - s2, s2 - s1
print '---'

# type casting
a = 'foo bar tuna'
b = (1, 2, 3, 4, 5, 4, 2, 1)
c = [66, 77, 88, 99]
d = {4, 6, 7, 8, 8}

print list(a), list(b), list(c), list(d)
print b, list(b)
print b, set(b)
print d, list(d)
print "-*-"
print b, str(b)
print c, str(c)
print str(4.567)

k = [3, 4, 5, 6, 7, 8, 9]
k[3:3] = [99, 98, 97]
print k

# strings
print "---"
a = ' hello woRld    '
print a.rstrip()
print a.lstrip()
print a.strip()
print a.lstrip().capitalize()
print a.upper()
print a.lower()
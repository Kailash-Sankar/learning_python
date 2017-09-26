a = [45, 67, 74, 33, 21]

b = a  # creates a reference
c = a[:]  # creates a copy

c.append(0)

# any element is true
# all elements must be true
print any(a), any(c)
print all(a), all(c)


def mypop(x):
    return x.pop()


# by default variables are passed by reference
print 'Call by reference'
print a
print mypop(a)
print a

# pass value using slice
print 'Call by value'
print a
print mypop(a[:])
print a


# passing dict by value
def moddict(d, key):
    d[key] = 22;


p = {4: 5, 5: 6, 6: 7}

print p
moddict(p, 5)
print p
moddict(p.copy(), 6)
print p

# the p.copy performs shallow copy
import copy

k = {1: a, 2: c}
l = copy.deepcopy(k)
print k, '||', l
a.append(88)
print k, '||', l

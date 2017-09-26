a = [4, 5, 6, 6 - 3, -3, -8, -5, 12]

print sorted(a)

a.sort()
print a

a.sort(key=lambda x: abs(x))
print a

a.sort(key=lambda x: x * -1)
print a

# comprehension
c = [x * x for x in a]
print c

d = [x % 2 for x in a]
print d

# not the right way if you want a shorter list
# if requires else
e = [x if x % 2 == 0 else None for x in a]
print e

# gives a shorter list
# if can be independent
d = [x for x in a if x % 2 == 0]
print d

# dict from list
d = {x: 2 * x for x in a}
print d

# set from list
l = {x for x in a}
print l

n = dict([(3, 4), (6, 7), (8, 9)])
print n

p = dict([ x.strip().split('=') for x in open("settings.txt") if not x.lstrip().startswith('#') ])
print p


del dict['TMP']
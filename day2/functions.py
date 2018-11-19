# functions
import functools

def pt(x):
    print(type(x))


pt([])
pt(23)
pt(3.4)
pt(pt)
pt(lambda x: x * x)
pt(None)


def applier(a, b, f):
    print(f(a, b))


applier(3, 5, lambda x, y: x + y)
applier(4, 6, lambda x, y: x * y)

games = ['csgo', 'astroneer', 'witness', 'Talos Principle','extra']
ratings = [90, 80, 89, 95]

print(zip(games, ratings))
print(list(zip(games, ratings)))

print(dict(zip(games, ratings)))
print(dict(zip(games, ratings))['astroneer'])
print("---")

a = [6, 7, 8, 2, 3]
print(list(map(lambda x: x ** 2, a)))

# iterator picks up only the keys
b = {10: 'alpha', 20: 'beta', 30: 'gamma'}
print(list(map(lambda x: x, b)))
for x in b: print(x,end=' ')
print()

# reduce
print("---")
print(functools.reduce(lambda x, y: x * y, a))
print(functools.reduce(lambda x, y: x + y / 2, a))

# map:    n => n
# reduce: n => 1
# filter: n => <= n

print("---")
print(list(filter(lambda x: x % 2, a)))
print(list(filter(lambda x: not x % 2, a)))
print(list(filter(lambda x: 1 if x % 2 == 0 else 0, a)))
a = [56,67,66,89,2]

#stack
a.append(56)
print(a.pop())

#queue
a.append(98)
print(a.pop(0))

# naming operations
push = a.append
pop = a.pop

push(45)
push(789)
print(pop())

add = a.append
remove = a.pop


add(78)
print(remove(0))
print(a)

# dictionary operations
print("---")
z = {6: 'hello', 7: 'world', 8: 2, 9: 67}

print(z.items(), z.keys(), z.values())

z[90] = 'howdy'

print(z[90], z.get(90))

z['hash'] = {'one': [1,2,4,5], 'two':[5,6,7,8]}

print(len( z['hash']['one'] ))

add = lambda x,y: x['hash']['one'].append(y)
add(z,'89')

print(len(z['hash']['one']))

checkKey = lambda x,y: x[y] if y in x else 'no key'

print(checkKey(z,'one'))
print(checkKey(z,'hash'))
print(z.get('two', 'No key!'))

#directly looking up the key will throw an exception, get is better
# print z['wiggle']
print(z.get('wiggle'))

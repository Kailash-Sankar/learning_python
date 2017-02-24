#closures

def createtitle(base):
    sub = 'meh'
    def createFancyTitle():
        return base + ' ' + sub
    return createFancyTitle

print createtitle('Pikachu')

avatar1 = createtitle('Muffin')
avatar2 = createtitle('Wookie')
print avatar1(),avatar2()
print "---"

def convert(x):
    def do(a):
        return a*x
    return do

mm = convert(1000)
cm = convert(100)
m = convert(1)
km = convert(1/1000.0)

distance_in_mtrs = 145

print mm(distance_in_mtrs)
print cm(distance_in_mtrs)
print m(distance_in_mtrs)
print km(distance_in_mtrs)
print "---"

for x in mm,cm,m,km:
    print id(x)
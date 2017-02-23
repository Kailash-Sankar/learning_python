# functions

def sub(a,b,c=100): #default arguments
    return a - b + c

print sub(4,56)
print sub (4,8,4)    #positional parameters
print sub (b=10,a=5) #keyword parameters

def sumdiff(a,b):
    return a+b,a-b

print sumdiff(45,45),sumdiff(4,5),sumdiff(7,10)

x,y = sumdiff(89,1)
print x,y

def addMany(*args):
    print type(args)
    print sum(args),min(args),max(args)


#got type error
p = lambda x,y: (x+y,x-y)
print p(12,2)


def avgThis(*args):
    return sum(args)/float(len(args)) #type cast at least one number to float

print avgThis(4,6,19,1,20)
print avgThis(4,5)

def avgThis2(a,b,*args):
    return ( a + b +sum(args) )/(len(args)+2.0) #adding 2.0 does the type casting for us

print avgThis2(4,5)


def avgThis3(*args):
    if ( len(args) < 2 ):
            print "Minimum 2 args required"
    else:
        return sum(args) / float(len(args))  # adding 2.0 does the type casting for us


print avgThis3(4, 5)
print avgThis3()

def magik(**kwargs):
    print type(kwargs)
    print len(kwargs)
    print kwargs


magik()
magik(alpha=23,beta=67,gamma=578)
magik(alpha="hello",BeTa="world")


def create_emp(id,name,**kwargs):
    print id,name,kwargs
create_emp(12,'kailash',work='WF',hours=8)


def super_flexible_function(*args,**kwargs):
    pass

def lowPoly(a,b,c,*sides,**options):
    print a,b,c,sides
    print options

    return a + b + c + sum(sides)

print lowPoly(4,5,6,9,10,unit="sqcm")
print lowPoly(5,6,1)

mul = lambda a,b:a*b
pow = lambda a,b:a**b
rept = lambda a,b: a+b * a-b

print type(mul)
print mul(2,3)
print pow(2,3)
print rept(2,3)

age = 20
def gloo():
    global age #by default global variables are readonly
    print age
    age = age + 10
    print age

gloo();
print age

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it"
    print "-- Lovely plumage, the", type
    print "-- it's ", state, "!"


parrot(100)
parrot('100')
parrot(100, action='wiggle')

parrot(110, voltage=220)  # duplicate value for an argument
parrot(voltage=5.0, "dead")  # non keyword argument following keyword
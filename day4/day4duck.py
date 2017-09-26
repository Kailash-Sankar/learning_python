# you can dynamically add attributes and methods to an object

# duck typing
# behave like a duck but without being a duck
class Car(object):
    def __init__(self, seats):
        self.seats = seats
        self.regno = None
        self.passengers = []

    def register(self, regno):
        self.regno = regno
        # these are called magic methods in python class

    def __len__(self):
        return self.seats

    def __str__(self):
        return "I am a {} seater car".format(self.seats)

    # works in if context and on bool type casts
    def __nonzero__(self):
        return bool(self.regno)

    # destructor should not be used for running important functionality
    # no guarantee on it getting called
    def __del__(self):
        print "deleted"

    # emulating the '+'
    # other doesn't have to be of type Car, it just needs to quak (duck typing)
    def __add__(self, other):
        return self.seats + other.seats

    def __mul__(self, other):
        return self.seats * 2 + other.seats * 2

    # full fledged object comparison
    def __cmp__(self, other):
        if self.seats > other.seats:
            return 1
        elif self.seats < other.seats:
            return -1
        else:
            return 0

    def board(self,passenger):
        self.passengers.append(passenger)

    def list_passengers(self):
        for p in self.passengers:
            print '{},'.format(p),
        print

    def __iter__(self):
        self.count = 0
        return self
    def next(self):
        if self.count < len(self.passengers):
            r = self.passengers[self.count]
            self.count += 1
            return r
        else:
            raise StopIteration


zen = Car(5)
innova = Car(7)

# check why type of car is type
print type(zen), type(Car)

# check if an object is of a class
print isinstance(zen, Car)
print isinstance(4, int)

# dunder len gets invoked
print len(zen)

# dunder str gets invoked
print zen
print innova

zen.register('KA44551')

print bool(zen), bool(innova)

if zen:
    print  'Zen is registered'

if innova:
    print 'na na banana'
else:
    print 'innova is not registered'

print 'Adding two objects', zen + innova

print 'Multiplying two objects', zen * innova

# without __cmp__ the output is no consistent
# comment it out and try
print 'Comparing two objects 1', zen > innova
print 'Comparing two objects 2', zen < innova
print 'zen', bool(zen)
print 'inno', bool(innova)
print 'test cmp', True > False

# this call explicitly invokes __del__ destructor
del innova
print 'giggity giggity'


# forward iterators
# iter() and next()
print '*'*5,'Iter','*'*5
zen.board('Hulk')
zen.board('Captain')
zen.board('Iron Man')
zen.board('Archer')

zen.list_passengers()

print 'iterating the object'
for z in zen:
    print z

print '*'*5,'Iter','*'*5
'''
singleton - only one object
factory - class creates and returns objects of similar classes
command pattern - have class with undo option
event handling - hierarchy of events bubbling up
'''

'''
class Singleton(object):
  _instances = {}
  def __new__(class_, *args, **kwargs):
    if class_ not in class_._instances:
        class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
    return class_._instances[class_]

class MyClass(Singleton):
  pass

c = MyClass()
b = MyClass()

print c is b
'''


# Simpler looking code
def section1():
    class Singleton(object):
        _c = {}

        # by default new is a class method
        def __new__(cls):
            if cls not in cls._c:
                cls._c[cls] = super(Singleton, cls).__new__(cls)
            return cls._c[cls]

    class MyClass(Singleton):
        def info(self):
            # check how to print super of a class
            print super(MyClass)
            print super(Singleton)

    c = MyClass()
    b = MyClass()

    c.info()

    class YourClass(Singleton):
        pass

    j = YourClass()
    k = YourClass()

    print k is j
    print c is b

    print Singleton._c


def section2():
    class Cup:
        color = ""

        # This is the factory method
        @staticmethod
        def getCup(cupColor):
            if (cupColor == "red"):
                return RedCup()
            elif (cupColor == "blue"):
                return BlueCup()
            else:
                return None

    class RedCup(Cup):
        color = "red"

    class BlueCup(Cup):
        color = "blue"

    # A little testing
    redCup = Cup.getCup("red")
    print "%s(%s)" % (redCup.color, redCup.__class__.__name__)

    blueCup = Cup.getCup("blue")
    print "%s(%s)" % (blueCup.color, blueCup.__class__.__name__)


def section3():
    # Code courtesy: http://stackoverflow.com/users/137839/mattyw
    class Handler:
        def __init__(self, parent=None):
            self.parent = parent

        def Handle(self, event):
            handler = 'Handle_' + event
            if hasattr(self, handler):
                self.handler.Handle(event)
            elif self.parent:
                self.parent.Handle(event)

    class Geo():
        def __init__(self, h):
            self.handler = h

        def Handle(self, event):
            # func = getattr(self.handler, 'Handle')
            # func(event)
            self.handler.Handle(event)

    class Steve():
        def __init__(self, h):
            self.handler = h

        def Handle(self, event):
            self.handler.Handle(event)

    class Andy():
        def Handle(self, event):
            print 'Andy is handling %s' % (event)

    if __name__ == '__main__':
        a = Andy()
        s = Steve(a)
        g = Geo(s)
        g.Handle('lab on fire')


# section1()
# section2()
section3()

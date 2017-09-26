# oop concepts

# oops
# Attributes
# Methods
# Understanding 'self'
# Understanding private variables
# Understanding private methods
# Class Methods
# Static Methods
# Inheritance
# Multiple Inheritance

class Employee(object):
    _count = 0  # _ is used as a convention for private variables. Not enforced
    company = 'Delta'  # class variable shared among all objects

    def __init__(self, eid, name, mobile):
        self.eid = eid
        self.name = name
        self.mobile = mobile
        Employee._count += 1  # just using count will look for a global variable

    def get_mobile(self):
        return self.mobile

    def set_mobile(self, mobile):
        self.mobile = mobile

    # turning this to a class method using a decorator
    @classmethod
    def get_emp_count(klass):  # cannot put self here because there is not object instance
        return klass._count  # class is a keyword so using klass
        # return Employee._count # this removes the need to hard code class name

    @staticmethod  # a method which has no relation with the Employee class but it's packaged together
    def si(p, t, r):
        print p * t * r / 100


def section_one():
    ramesh = Employee(223, "Ramesh", '9885870033')
    print ramesh.name
    print ramesh.eid
    print ramesh.get_mobile()
    ramesh.set_mobile("9845567809")
    print ramesh.get_mobile()

    # Count is a private variable and should not be accessed directly
    print ramesh._count, Employee._count  # class variable can be accessed through object as well as the class
    sheldon = Employee(245, "Sheldon", '9885870044')
    print sheldon._count, ramesh._count  # see that it's available in both objects

    # best practise
    # accessing a method like this through object is not suitable in this case
    # employee count shouldn't require an employee object
    print sheldon.get_emp_count()
    print Employee.get_emp_count()

    # allowed
    ramesh.eid = 88
    print ramesh.eid

    # static methods cab be called from class and object
    ramesh.si(1000, 2, 2)
    Employee.si(800, 1, 8)


class Baby(object):
    # constructor, not mandatory
    def __init__(self, name):
        self.name = name

    def laugh(self):
        print 'ha..ha..ha'

    def cry(self):
        print 'I am crying'

    def hi(self):
        print 'Hello!! I am {}'.format(self.name)


def section_two():
    pinky = Baby('Haritha')
    pinky.laugh()
    pinky.cry()
    pinky.hi()
    print pinky.__dict__  # print all attributes as a hash


section_one()
print '*' * 10
section_two()

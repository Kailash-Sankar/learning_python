# decorators

def double(old_func):
    def new_func(*args, **kwargs):
        old_func(*args, **kwargs)
        old_func(*args, **kwargs)
    return new_func


def hello():
    print "Hello - Adele"


@double
def square(n): print n * n


@double
def add(a, b): print a + b


add(34, 23)
square(34)
hello()
print "---"

def double_in(old_func):
    def new_func(arg):
        return old_func(2 * arg)
    return new_func


def double_out(old_func):
    def new_func(*args, **kwargs):
        return 2 * old_func(*args, **kwargs)

    return new_func


@double_in
def twice(x):
    return 2 * x


@double_out
def thrice(x):
    return 3 * x


@double_in
@double_out
def five(x):
    return x * 5


print twice(3)
print thrice(3)
print five(2)


'''
built in
@classmethod
@staticmethod
@property
'''
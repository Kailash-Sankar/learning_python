import sys


class Squares(object):
    """Class to implement an iterator
    of squares of integers"""

    def __init__(self, max=0):
        self.max = max
        self.min = 1

    def __iter__(self):
        return self

    def next(self):
        if self.min <= self.max:
            result = self.min ** 2
            self.min += 1
            return result
        else:
            raise StopIteration


s10 = Squares(10)
print type(s10)

for square in Squares(50):
    pass
    # print square

print sys.getsizeof(s10)

'''
range size consumption difference between p27 and p3 for range of a huge number
'''


def countdown(x):
    while x > 0:
        yield x  # returns an iterable object with value of x
        x -= 1


a = countdown(10)
print type(a)

for x in a: print x

# using list comprehension for making a generator
xl = [x * x for x in range(1, 26)]
xd = (x * x for x in range(1, 26))

print xd
print xd.next(), xd.next()

# generator size remains the same even if the range goes up
print sys.getsizeof(xl)
print sys.getsizeof(xd)

# you can type cast a generator in to a list. Cool.
z = list(xd)
print sys.getsizeof(z)

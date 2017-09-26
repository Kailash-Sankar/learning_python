import datetime, math, os
from threading import Thread

load = 25000
iterations = 30


def fact(n):
    print 'process id:', os.getpid()
    print len(str(math.factorial(load + n)))
    return


# Sequential processing block
start = datetime.datetime.now()
for i in range(iterations): fact(i)
end = datetime.datetime.now()
t1 = end - start
# Multi threading block
start = datetime.datetime.now()
threads = []
for i in range(iterations):
    t = Thread(target=fact, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
end = datetime.datetime.now()
t2 = end - start
# raw_input('continue?')
print 'Normal Processing Time:', t1
print 'Multi Threading Time:', t2

# GIL - global interpreter lock

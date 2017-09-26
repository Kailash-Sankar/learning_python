import datetime, time, math, os
from multiprocessing import Process

load = 15000
iterations = 25


def fact(n):
    print 'process id:', os.getpid()
    print len(str(math.factorial(load + n)))

if __name__ == '__main__':
    print "Sequential processing block"
    start = datetime.datetime.now()
    for i in range(iterations): fact(i)
    end = datetime.datetime.now()
    t1 = end - start

    print "Multi processing block"
    start = datetime.datetime.now()

    procs = []
    for i in range(iterations):
        p = Process(target=fact, args=(i,))
        procs.append(p)
        p.start()
    for t in procs:
        t.join()

    end = datetime.datetime.now()
    t3 = end - start

    print 'Sequential',t1
    print 'Multi',t3

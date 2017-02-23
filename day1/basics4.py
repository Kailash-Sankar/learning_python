# ranges and enumeration
for x in range(3): print x, #add comma to print on the same line
print #this will close of the comma

for x in range(4,5): print x, #till the last index
print

for x in 4,5,6,23,45,56: print x,
print

for x in {4:5,2:56,5:33}: print x,
print

for x in {4:5,2:56,5:33}.values(): print x,
print

for x,y in {4:5,2:56,5:33}.items(): print x,'=>',y,
print

#unpacking variable. if the numbers don't match an error will be thrown
for x,y in {4:5,2:56,5:33}.items(): print '{} ==> {}'.format(x,y),
print

# iterator object
for x in enumerate([1,4,8,45,2]): print x,
print

for x in enumerate((1,4,8,45,2)): print x,
print

for x in enumerate({1,4,8,45,2}): print x,
print


# accepting user input
if 0:
    for x in range(3):
        amt = raw_input('Enter amount')
        if int(amt) % 100 == 0:
            print 'please collect the cash'
            break
        else :
           print 'Error: Enter a valid amount'
    else:
        print "Try again"



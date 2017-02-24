# read csv file and print files greater than 1MB
fin = open('HourlyHits.csv', 'r')
c = 0
for line in fin:
    date, name, size = line.split(',')
    if int(size) > 1000000:
        c = c + 1
        print name, size

print 'Total number of files greater than 1MB', c
fin.close();

# read settings file to dict, but ignore lines starting with '#'
# also ignore empty lines
fd = open('settings.txt', 'r')
myenv = {}
for line in fd:
    line = line.strip()
    if line and not line.startswith('#'):
        key, value = line.split('=')
        myenv[key] = value
print myenv


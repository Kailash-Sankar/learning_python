# file handling

# open file for reading
fin = open('settings.txt', 'r')

# line by line
print fin.readline()
print fin.readline()
print "---"

# char by char
print fin.read(1)
print fin.read(3)
print "-*-"

# check status
print fin.closed

print fin.readline().rstrip()  # rstrip removes all whitespace, newlines
print fin.readline().rstrip('\n')  # now it removes only new lines
print "-**-"

print fin.read()  # read the whole file

fin.close()
print fin.closed

fin = open('settings.txt', 'r')

lines = fin.readlines()
print lines[::2]
print lines[-1]

fin.close()

fout = open('set.txt', 'a')  # full path can have double backslash or forward slash
fout.write('Shiver Me Timbers')
fout.write(', yup \n')

x = ['Start', 'the', 'game', '\n']
fout.writelines(x)

fout.close();
fin = open('set.txt', 'r')
for line in fin:
    print line,
fin.close()

print '*' * 10
fin = open('settings.txt', 'r')
print fin.tell()
print fin.readline().rstrip()
print fin.tell()
print fin.read(2)
print fin.tell()
print "---"

'''
seek(n,m)
n offset from position indicated by m
m => 0 - beginning of file, 1 - current position, 2 - end of file
'''

fin.seek(0, 0)
print fin.tell()
print fin.readline().rstrip()
fin.seek(-10, 1)
print fin.tell()
print fin.readline().rstrip()


fin.close()

'''
Additional modes
r+ - read and overwrite until EOF
a+ - read and append. Auto seeks to end of file
w+ - read, write and overwrite content
'''

# split
print "---"
a = 'alpha,beta,gamma'
print a.split(",")

x, y, z = a.split(',')
print x, y, z

print "ba ba blacksheep ba ba blacksheep"[6:16]

'''
compare two files, by default it's shallow (like comparison using os stat)
deep comparison is expensive

import filecmp
print filecmp.cmp('file1.txt','file2.txt')
print filecmp.cmp('file1.txt','file2.txt',shallow=False)
'''

'''
u"Hello" - unicode
r"\n\n\t" - raw string
'''

import os, glob, zipfile,time


def zipstuff():
    print os.getcwd()
    os.chdir('C:\\Users\\almaz\\Desktop\\dev')
    print os.getcwd()

    files = glob.glob('*.py')
    print 'Compressing', len(files), 'files'

    z = zipfile.ZipFile('C:\\Users\\almaz\\Desktop\\wf.zip', 'w', zipfile.ZIP_DEFLATED)

    for fle in files:
        z.write(fle)
    print type(z)

    z.close()
    zip_ratio()


def zip_ratio():
    zfs = os.stat('C:\\Users\\almaz\\Desktop\\wf.zip').st_size
    tfs = 0
    for file in glob.glob('*.py'):
        tfs += os.stat(file).st_size
    print 'Total file size:', tfs
    print 'Zip file size:', zfs
    print 'Compression ratio', zfs / float(tfs)


def unzip():
    targetdir = 'C:\\Users\\almaz\\Desktop\\unzip\\'
    z = zipfile.ZipFile('C:\\Users\\almaz\\Desktop\\wf.zip','r')

    for file in z.namelist():
        fin = z.open(file)
        fout = open(targetdir + file,'w')
        fout.write(fin.read())
        fin.close()
        fout.close()
    z.close()


zipstuff()
time.sleep(2)
unzip()


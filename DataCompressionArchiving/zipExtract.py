import zipfile
import os.path

zfile = zipfile.ZipFile("TestFormats.zip")
for name in zfile.namelist():
    (dirname, filename) = os.path.split(name)
    print "Decompressing " + filename + " on " + dirname
    # Check if the directory exisits
    if filename == '':
        # directory
        if not os.path.exists(dirname):
            os.mkdir(dirname)
    else:
        # file
        fd = open(name, 'w')
        fd.write(zfile.read(name))
        fd.close()
zfile.close()
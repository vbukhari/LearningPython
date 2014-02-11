import os.path
import tarfile, zlib, zipfile, gzip, bz2

#pwd= os.getcwd()
working_path = 'D:\\Dropbox\\AdvancePython\\Extracting'
with zipfile.ZipFile("TestFormats.zip") as zf:
 	zf.extractall(working_path)
 	print zf.namelist()

#	@author: Vasim Bukhari
#	Project 1 Advance Python: Universal Extractor
# Universal Extractor: an application that will take any number of files in an archived and/or 
# compression format, i.e., .zip, .tgz, .tar.gz, .gz, .bz2, .tar.bz2,  .tbz, and a target directory.
# The program will uncompress the stand-alone files to the target while all archived files will be 
# extracted into subdirectories named the same as the archive file without the file extension. 
# For example, if the target directory was incoming, and the input files were header.txt.gz and 
# data.tgz, header.txt will be extracted to incoming while the files in data.tgz will be pulled
# out into incoming/data.
import os.path
import sys
import tarfile, zipfile, gzip, bz2

def Extractor(filename, target):

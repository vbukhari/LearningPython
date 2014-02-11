#!/usr/bin/python
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


def main(argv):
	incoming = sys.argv[1]
	if not os.path.exists(incoming):
		os.mkdir(incoming)
	for x in argv[2:]:
		Extractor(incoming, x)

def Extractor(target, filename):
	(fname, extension) = os.path.splitext(filename)

	(subFileName, subExtension) = os.path.splitext(fname)
	subpath = target+"/"+subFileName

		#Extracting .zip
	if extension == ".zip":
		with zipfile.ZipFile(filename) as zf:
			zf.extractall(target)
	#Extracting .tar.gz, .txt.gz, .tgz files
	elif extension ==".gz" or extension == ".tgz":
		if subExtension == ".txt":
			with gzip.GzipFile(filename) as tar:
				tar.extractall(target)
	 	elif subExtension == ".tar":
	 		if not os.path.exists(subpath):
				# os.mkdir(gzFileName)
				os.mkdir(subpath)
	 		with tarfile.open(filename, 'r:gz') as tar:
	 			tar.extractall(subpath)
	 		# print "Hello1!!"
	 	else:
	 		if not os.path.exists(subpath):
				os.mkdir(subpath)
	 		with tarfile.open(filename, 'r:gz') as tar:
	 			tar.extractall(subpath)
	 		# print "Hello2!!"
	#Extracting .tar.bz2, .txt.bz2, tbz files
	elif extension == ".bz2" or extension == ".tbz":
		if subExtension == ".txt":
			with gzip.GzipFile(filename) as tar:
				tar.extractall(target)
	 	elif subExtension == ".tar":
	 		if not os.path.exists(subpath):
				os.mkdir(subpath)
	 		with tarfile.open(filename, 'r:bz2') as tar:
	 			tar.extractall(subpath)
	 	else:
	 		if not os.path.exists(subpath):
				os.mkdir(subpath)
	 		with tarfile.open(filename) as tar:
	 			tar.extractall(subpath)
	#Extracting .tar file
	elif extension == ".tar":
		with tarfile.TarFile(filename) as tar:
			tar.extractall(target)
	else:
		print "file not found"


if __name__ == '__main__':
	main(sys.argv)
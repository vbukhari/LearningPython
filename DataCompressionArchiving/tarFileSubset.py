import os.path
import tarfile

# def py_files(members):
#     for tarinfo in members:
#         if os.path.splitext(tarinfo.name)[1] == ".py":
#             yield tarinfo

# tar = tarfile.open("test.tar.gz")
# tar.extractall(members=py_files(tar))
# tar.close()

# target = "incoming"
# if not os.path.exists(target):
# 	os.mkdir(target)
# filename = "test3.tar"
# fname, extension = os.path.splitext(filename)
# with tarfile.TarFile(filename) as tar:
# 	os.chdir(target)
# 	tar.extractall(os.mkdir(fname))

# def py_files(members):
#     for tarinfo in members:
#         if os.path.splitext(tarinfo.name)[1] == ".txt":
#             yield tarinfo

# tar = tarfile.open("test1.tar.gz")
# tar.extractall(members=py_files(tar))
# tar.close()

# target = "incoming"
# if not os.path.exists(target):
# 	os.mkdir(target)
# filename = "test.tar.gz"
# fname, extension = os.path.splitext(filename)
# with tarfile.open(filename, "r:gz") as tar:
# 	print tar.add(target, arcname=os.path.basename(target))

# tar = tarfile.open("test3.tar")
# for member in tar:
# 	print member
# 	tar.extractall(os.mkdir("Hello"))
# tar.close()

# theTarFile = "test3.tar"
# extractTarPath = '.'
# tfile = tarfile.open(theTarFile)
# if tarfile.is_tarfile(theTarFile):
# 	print "tar file contents: "
# 	print tfile.list(verbose=False)
# 	tfile.extractall(extractTarPath)
# else:
# 	print theTarFile + "is not a tarfile"

# with tarfile.open("dir.tar") as tar:
# 	subdir = [tarinfo for tarinfo in tar.getmembers()]
# 	tar.extractall(members=subdir)

target = "incoming"
if not os.path.exists(target):
 	os.mkdir(target)
with tarfile.open("test3.tar") as tar:
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar, target)
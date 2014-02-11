#	@author: Vasim Bukhari
#	Practice problem for compressing and decompressing gzip files
import os
import gzip

#Create a compressed GZIP file and write content
content = "Lots of content here"
f = gzip.open('file.txt.gz', 'wb')
f.write(content)
f.close()

#GZIP compress an existing file
f_in = open('file.txt', 'rb')
f_out = gzip.open('file2.txt.gz', 'wb')
f_out.writelines(f_in)
f_in.close()
f_out.close()

#Read a compresed  GZIP file
f = gzip.open('file.txt.gz', 'rb')
file_content = f.read()
f.close()



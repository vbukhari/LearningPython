import os, sys, tarfile

def main(argv):
    incoming = sys.argv[1]
    if not os.path.exists(incoming):
        os.mkdir(incoming)
    for x in argv[2:]:
        # Extractor(incoming, x)
        ExtractFile(incoming, x)
        print 'Done.'


def ExtractFile(filename, target):
    print "Hellooo"
    tar = tarfile.open(filename, 'r:gz')
    print "Hello2"
    for item in tar:
        print "Hello4"
        tar.extract(item, tar)
        if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1:
            extract(item.name, "./" + item.name[:item.name.rfind('/')])
    print "Hello3"
# try:

#     ExtractFile(sys.argv[1] + '.tgz', )
#     print 'Done.'
# except:
#     name = os.path.basename(sys.argv[1])
#     print "Hello1"
    # print name[:name.rfind('.')], '<filename>'
if __name__ == '__main__':
    main(sys.argv)
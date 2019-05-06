#I just want to print Mogege from hello.txt version 1.1
#xFile = open('hello.txt','r')
#for moge in xFile:
#    if moge.startswith('Moge'):
#        print(moge.rstrip())

#=====================This is version 1.2 to print Mogege
xFile = open('hello.txt','r')
for moge in xFile:
    if not moge.startswith('Moge'):
        continue
    print(moge.rstrip())

flist = list()
cwlist = list()
ydoc = open('romeo.txt')

for line in ydoc:
    words=line.split()
    for word in words:
        if word in flist:
            if word not in cwlist:
                cwlist.append(word)
            continue
        flist.append(word)
flist.sort()
print(flist)
cwlist.sort()
print(cwlist)

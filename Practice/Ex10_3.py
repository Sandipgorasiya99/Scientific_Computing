doc = open('mbox-short.txt')
hdict = dict()

for line in doc:
    line=line.rstrip()
    words=line.split()
    if len(words)>5 and line.startswith('From'):
        hword=words[5].split(':')
        hdict[hword[0]]=hdict.get(hword[0],0)+1

fdict = dict()
for k,v in sorted(hdict.items()):
    print(k,v)

nlist=[]
for k,v in hdict.items():
    newvalue=v,k
    nlist.append(newvalue)
print(sorted(nlist, reverse=True))

#Sort the hightest emailed received in hours to lowest
for x in sorted(nlist, reverse=True):
    print(x[1],x[0])

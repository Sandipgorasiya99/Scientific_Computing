doc = open('mbox-short.txt')
hdict = dict()

for line in doc:
    line=line.rstrip()
    words=line.split()
    if len(words)>5 and line.startswith('From'):
        hword=words[5].split(':')
        hdict[hword[0]]=hdict.get(hword[0],0)+1

for k,v in sorted(hdict.items()):
    print (k,v)

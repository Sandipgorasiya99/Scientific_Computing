doc= input('Enter the file name:')
wdoc=open(doc)
sndcount = {}
for line in wdoc:
    line=line.rstrip()
    word = line.split()
    # if len(line)>3 and word[0]==('From'):
    if line.startswith('From') and len(word)>3:
        #print(word[1])
        sndcount[word[1]] = sndcount.get(word[1], 0) +1
    else:
        continue
print(sndcount)
lcount = None
lkey = None
for key,value in sndcount.items():
    if lcount == None or value > lcount:
        lcount = value
        lkey = key
print(lkey, lcount)

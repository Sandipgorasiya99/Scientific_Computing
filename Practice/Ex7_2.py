doc=input('Filename:')
han= open(doc)

def search(x):
    str=x
    ipos = str.find(':')
    piece = str[ipos+1:]
    value=float(piece)
    return value

count=0
total=0
for line in han:
    line=line.rstrip()
    if 'X-DSPAM-Confidence' in line:
        val = search(line)
        count = count+1
        total = total + val

print('Average spam confidence:', total/count)

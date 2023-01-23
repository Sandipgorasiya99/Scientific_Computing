han= open('mbox-short.txt')
count=0
for line in han:
    line=line.rstrip()
    if line.startswith('From:'):
        count=count+1
print(count)

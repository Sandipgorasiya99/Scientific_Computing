import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}
Total=0
for line in fhand:
    words=line.decode().split()
    for word in words:
        Total =  Total + 1
        counts[word] = counts.get(word,0)+1
print(Total)
print(counts)

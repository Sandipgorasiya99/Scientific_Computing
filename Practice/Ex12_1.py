import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
counts = {}
Total=0
for line in fhand:
    words=line.decode().split()
    print(line.decode().strip())
    for word in words:
        Total =  Total + 1
        counts[word] = counts.get(word,0)+1
print(Total)
print(counts)

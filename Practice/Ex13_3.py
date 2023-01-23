import urllib.request , urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

url = input ('Enter URL: ')
print('Retriving', url)
uh = urllib.request.urlopen(url,context=ctx)

data=uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())

tree = json.loads(data)

print(tree)
total=0
cnt= tree['comments']

for val in cnt:
    cnt= val['count']
    print(cnt)
    total=total+cnt
print(total)

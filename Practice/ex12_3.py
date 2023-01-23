import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Winnifred.html"
pos = input('Position: ')
rpt = input('Repeat: ')
lp = 0
while lp < int(rpt):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')
    url = tag[int(pos)-1].get('href', None)
    print(url)
    lp=lp+1

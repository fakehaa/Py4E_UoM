import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' #test
url = 'http://py4e-data.dr-chuck.net/known_by_Coco.html'    #actual url to test

count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(count):
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[position-1].get('href', None)

last_name = tags[position-1].text

print('Last name in the sequence:', last_name)

# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

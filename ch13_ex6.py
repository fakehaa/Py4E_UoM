import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2373107.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = []
for result in counts:
    # Debug print the data :)
    result = nums.append(int(result.text))
    print('Count:', len(nums))
    print('Sum:', sum(nums))
    #print(result.text)


print('Count final:', len(nums))
print('Sum final:', sum(nums))


import xml.etree.ElementTree as ET
import urllib

url=raw_input('enter url')
fh=urllib.urlopen(url).read()
data=ET.fromstring(fh)
lst=data.findall('.//count')
sum=0
for item in lst:
	sum=sum+int(item.text)
print sum;
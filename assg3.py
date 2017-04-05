import urllib
import json

url=raw_input("enter url : ")
data=urllib.urlopen(url).read()
info=json.loads(data)
sum=0
for item in info['comments']:
	print item
	sum=sum+item['count']
print 'sum : ',sum
import urllib
from BeautifulSoup import *
url=raw_input('Enter url-')
c=raw_input('Count : ')
count=int(c)
p=raw_input('pos : ')
pos=int(p)
i=1
print url

while i<=count:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	url=tags[pos-1].get('href',None)
	print url
	i=i+1
	
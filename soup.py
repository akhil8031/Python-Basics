import urllib
from BeautifulSoup import *
html = urllib.urlopen('http://python-data.dr-chuck.net/comments_289081.html').read()
soup = BeautifulSoup(html)

tags = soup('span')
sum=0
for tag in tags:
	sum=sum+int(tag.contents[0])
print sum
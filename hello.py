import re
fh=open('data.txt')
str=fh.read()
y=re.findall('[0-9]+',str)
y=map(int,y)
print sum(y)
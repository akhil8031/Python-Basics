import urllib
import json
serviceurl = 'http://python-data.dr-chuck.net/geojson?'
while True:
	address = raw_input('Enter location: ')
	if len(address) < 1 : break
	url = serviceurl + urllib.urlencode({'sensor':'false','address': address})
	print url
	uh = urllib.urlopen(url)
	data = uh.read()
	js = json.loads(str(data))
	location = js['results'][0]["place_id"]
	print location
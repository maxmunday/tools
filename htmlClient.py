#!/usr/bin/python
# HTML Client 
# www.maxmunday.com

import urllib2

html = urllib2.urlopen('http://vulnerable/')

print html.read()

html.close()
#!/usr/bin/python
# HTTP Client 
# www.maxmunday.com

import urllib2

r = urllib2.urlopen('http://vulnerable/')

print r.read()

r.close()

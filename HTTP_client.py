#!/usr/bin/python
# HTTP Client with Header Info
# www.maxmunday.com

import httplib

# connect to HTTP server, send GET request, receive response
h = httplib.HTTPConnection('vulnerable')
h.request('GET', '')
r = h.getresponse()

# get and print HTTP header response
rh = r.getheaders()
print 'Header:'
for i in rh:
    print i[0], ':', i[1]
print '\n'

# get and print content of response
rr = r.read()
print 'Content:'
print rr
print '\n'

# close HTTP connection to server
h.close()

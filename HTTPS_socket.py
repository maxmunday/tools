#!/usr/bin/python
# HTTPS Socket Client 
# www.maxmunday.com

import socket
import ssl

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# wrap socket
wrapSock = ssl.wrap_socket(s)

# connect and print reply
wrapSock.connect(("vulnerable", 443))
wrapSock.sendall("GET /\r\n")
print wrapSock.recv(4096)

wrapSock.close
